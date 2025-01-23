class BaseClass:
    def __init__(self, layer_name):
        """
        Initialize BaseClass with layer_name.
        """
        self.layer_name = layer_name
        self.database_read = "D:/MDH//Connections2/MDH DEV mdhephtdbdev1 to _MDHEPHT_ via READ.sde"

    # Config properties common to all instances
    import_modules = "import arcpy from sys import argv"
    allow_overwriting_output = "arcpy.env.overwriteOutput = True"
    database_read = "D:/MDH//Connections2/MDH DEV mdhephtdbdev1 to _MDHEPHT_ via READ.sde"
    scratch_gdb = ".../mdh-epht-gis-utilities/WorkingDocument/Scratch.gdb"
    output_gdb = ".../mdh-epht-gis-utilities/WorkingDocument/Outputs.gdb"

class CommonLayer(BaseClass):
    def __init__(self, layer_name, year, geometry, database_table, existing_layer, geometry_layer, expression, 
                 input_join_field, target_join_field, output_layer, copy_geometry_to_scratch_gdb, 
                 query_table_from_db_table, save_query_table_to_scratch_gdb, join_queried_table_to_geometry, 
                 copy_layer_to_output_gdb, delete_rows_from_existing_layer, append_queried_table_to_existing_layer):
        """
        Initialize CommonLayer with all its attributes.
        """
        super().__init__(layer_name)
        self.year = year
        self.geometry = geometry
        self.database_table = database_table
        self.existing_layer = existing_layer
        self.geometry_layer = geometry_layer
        self.expression = expression
        self.input_join_field = input_join_field
        self.target_join_field = target_join_field
        self.output_layer = output_layer
        self.copy_geometry_to_scratch_gdb = copy_geometry_to_scratch_gdb
        self.query_table_from_db_table = query_table_from_db_table
        self.save_query_table_to_scratch_gdb = save_query_table_to_scratch_gdb
        self.join_queried_table_to_geometry = join_queried_table_to_geometry
        self.copy_layer_to_output_gdb = copy_layer_to_output_gdb
        self.delete_rows_from_existing_layer = delete_rows_from_existing_layer
        self.append_queried_table_to_existing_layer = append_queried_table_to_existing_layer

    def copy_geo(self, source, destination):
        """
        Simulate copying geographical data from source to destination.
        """
        print(f"Copying data from {source} to {destination}.")


class Asthma(CommonLayer):
    def __init__(self, layer_name, output_layer, geometry, geometry_layer, existing_layer, expression, input_join_field,
                 target_join_field):
        """
        Initialize Asthma with its specific attributes.
        """
        database_table = f"{self.database_read} + 'MDHEPHT.epht.Asthma_NCDM_' + {geometry}"
        existing_layer = f"{self.database_read} + {existing_layer}"
        geometry_layer = f"{self.database_read} + {geometry_layer}"
        expression = expression
        input_join_field = input_join_field
        target_join_field = target_join_field
        copy_geometry_to_scratch_gdb = f"{self.copied_geometry} = arcpy.management.CopyFeatures({geometry_layer}, {self.scratch_gdb} + 'Copied_Geometry')"
        query_table_from_db_table = f"{self.query_table} = arcpy.management.MakeQueryTable({database_table}, 'Query_Table')"
        save_query_table_to_scratch_gdb = f"{self.queried_table} = arcpy.conversion.TableToTable({self.query_table}, {self.scratch_gdb}, 'Queried_Table', {expression})"
        join_queried_table_to_geometry = f"{self.geometry_with_join} = arcpy.management.JoinField({self.copied_geometry}, {input_join_field}, {self.queried_table}, {target_join_field})"
        copy_layer_to_output_gdb = f"{self.copied_layer} = arcpy.conversion.FeatureClassToFeatureClass({existing_layer}, {self.output_gdb}, {output_layer})"
        delete_rows_from_existing_layer = f"{self.empty_layer} = arcpy.management.DeleteRows({self.copied_layer})"
        append_queried_table_to_existing_layer = f"arcpy.management.Append({self.geometry_with_join}, {self.output_gdb} + {output_layer}, 'NO_TEST')"

        super().__init__(layer_name, self.year, geometry, database_table, existing_layer, geometry_layer, expression, 
                         input_join_field, target_join_field, output_layer, copy_geometry_to_scratch_gdb, 
                         query_table_from_db_table, save_query_table_to_scratch_gdb, join_queried_table_to_geometry, copy_layer_to_output_gdb,
                         delete_rows_from_existing_layer, append_queried_table_to_existing_layer)

    # Properties that are common to all instances for Asthma
    year = 2025
    copied_geometry = None  # Placeholder for dynamically created variable that will need to be set to result of copy_geometry_to_scratch_gdb
    query_table = None  # Placeholder for dynamically created variable that will need to be set to result of query_table_from_db_table
    queried_table = None  # Placeholder for dynamically created variable that will need to be set to result of save_query_table_to_scratch_gdb
    geometry_with_join = None  # Placeholder for dynamically created variable that will need to be set to result of join_queried_table_to_geometry
    copied_layer = None  # Placeholder for dynamically created variable that will need to be set to result of copy_layer_to_output_gdb
    empty_layer = None  # Placeholder for dynamically created variable that will need to be set to result of delete_rows_from_existing_layer

class AsthmaCounty(Asthma):
    def __init__(self, layer_name, output_layer, existing_layer, expression):
        """
        Initialize CountyAsthma with its specific attributes.
        """
        super().__init__(layer_name, output_layer, self._geometry, self._geometry_layer, 
                         existing_layer, expression, self._input_join_field, self._target_join_field)
    
    # Properties that are specific to County instances 
    _geometry = "County"
    _geometry_layer = "MDHEPHT.EPHT.GIS_County_Poly"
    _input_join_field = "MD_CODE"
    _target_join_field = "MDCODE"


class AsthmaCensusTract(Asthma):
    def __init__(self, layer_name, output_layer, existing_layer, expression):
        """
        Initialize CensusTractAsthma with its specific attributes.
        """
        super().__init__(layer_name, output_layer, self._geometry, self._geometry_layer,
                         existing_layer, expression, self._input_join_field, self._target_join_field)
    
    # Properties that are specific to CensusTract instances     
    _geometry = "CensusTract"
    _geometry_layer = "MDHEPHT.EPHT.GIS_CensusTract20_Poly"
    _input_join_field = "GEOID"
    _target_join_field = "TRACTCODE"




# Example usage
if __name__ == "__main__":
    # Create an instance of AsthmaCounty
    county_asthma_instance = AsthmaCounty(
        layer_name="Asthma_NCDM_GIS_AgeAdjusted_ED_County", 
        output_layer="Asthma_NCDM_GIS_AgeAdjusted_ED_County",
        existing_layer= "MDHEPHT.EPHT.Asthma_NCDM_GIS_AgeAdjusted_ED_County",
        expression= f"(TYPE_ID = 17) AND (YEAR = {Asthma.year}) AND (GROUPAGE_ID = 8)") 
    
    print("\n")
    print("CountyAsthma Instance:")
    print(f"Layer Name: {county_asthma_instance.layer_name}")
    print(f"import_modules: {county_asthma_instance.import_modules}")
    print(f"allow_overwriting_output: {county_asthma_instance.allow_overwriting_output}")
    print(f"database_read: {county_asthma_instance.database_read}")
    print(f"scratch_gdb: {county_asthma_instance.scratch_gdb}")
    print(f"output_gdb: {county_asthma_instance.output_gdb}")
    print(f"year: {county_asthma_instance.year}")
    print(f"geometry: {county_asthma_instance.geometry}")
    print(f"database_table: {county_asthma_instance.database_table}")
    print(f"existing_layer: {county_asthma_instance.existing_layer}")
    print(f"geometry_layer: {county_asthma_instance.geometry_layer}")
    print(f"expression: {county_asthma_instance.expression}")
    print(f"input_join_field: {county_asthma_instance.input_join_field}")
    print(f"target_join_field: {county_asthma_instance.target_join_field}")
    print(f"output_layer: {county_asthma_instance.output_layer}")
    print(f"copy_geometry_to_scratch_gdb: {county_asthma_instance.copy_geometry_to_scratch_gdb}")
    print(f"query_table_from_db_table: {county_asthma_instance.query_table_from_db_table}")
    print(f"save_query_table_to_scratch_gdb: {county_asthma_instance.save_query_table_to_scratch_gdb}")
    print(f"join_queried_table_to_geometry: {county_asthma_instance.join_queried_table_to_geometry}")
    print(f"copy_layer_to_output_gdb: {county_asthma_instance.copy_layer_to_output_gdb}")
    print(f"delete_rows_from_existing_layer: {county_asthma_instance.delete_rows_from_existing_layer}")
    print(f"append_queried_table_to_existing_layer: {county_asthma_instance.append_queried_table_to_existing_layer}")

    print("\n")

    # Create an instance of AsthmaCounty
    county_unadjusted_asthma_instance = AsthmaCounty(
        layer_name="Asthma_NCDM_GIS_Unadjusted_ED_County", 
        output_layer="Asthma_NCDM_GIS_Unadjusted_ED_County",
        existing_layer="MDHEPHT.EPHT.Asthma_NCDM_GIS_Unadjusted_ED_County",
        expression= f"(TYPE_ID = 18) AND (YEAR = {Asthma.year}) AND (GROUPAGE_ID = 8)")  
    
    print("CountyAsthma Instance2:")
    print(f"Layer Name: {county_unadjusted_asthma_instance.layer_name}")
    print(f"import_modules: {county_unadjusted_asthma_instance.import_modules}")
    print(f"allow_overwriting_output: {county_unadjusted_asthma_instance.allow_overwriting_output}")
    print(f"database_read: {county_unadjusted_asthma_instance.database_read}")
    print(f"scratch_gdb: {county_unadjusted_asthma_instance.scratch_gdb}")
    print(f"output_gdb: {county_unadjusted_asthma_instance.output_gdb}")
    print(f"year: {county_unadjusted_asthma_instance.year}")
    print(f"geometry: {county_unadjusted_asthma_instance.geometry}")
    print(f"database_table: {county_unadjusted_asthma_instance.database_table}")
    print(f"existing_layer: {county_unadjusted_asthma_instance.existing_layer}")
    print(f"geometry_layer: {county_unadjusted_asthma_instance.geometry_layer}")
    print(f"expression: {county_unadjusted_asthma_instance.expression}")
    print(f"input_join_field: {county_unadjusted_asthma_instance.input_join_field}")
    print(f"target_join_field: {county_unadjusted_asthma_instance.target_join_field}")
    print(f"output_layer: {county_unadjusted_asthma_instance.output_layer}")
    print(f"copy_geometry_to_scratch_gdb: {county_unadjusted_asthma_instance.copy_geometry_to_scratch_gdb}")
    print(f"query_table_from_db_table: {county_unadjusted_asthma_instance.query_table_from_db_table}")
    print(f"save_query_table_to_scratch_gdb: {county_unadjusted_asthma_instance.save_query_table_to_scratch_gdb}")
    print(f"join_queried_table_to_geometry: {county_unadjusted_asthma_instance.join_queried_table_to_geometry}")
    print(f"copy_layer_to_output_gdb: {county_unadjusted_asthma_instance.copy_layer_to_output_gdb}")
    print(f"delete_rows_from_existing_layer: {county_unadjusted_asthma_instance.delete_rows_from_existing_layer}")
    print(f"append_queried_table_to_existing_layer: {county_unadjusted_asthma_instance.append_queried_table_to_existing_layer}")

    print("\n")

    #  # Create an instance of CensusTractAsthma
    tract_asthma_instance = AsthmaCensusTract(
        layer_name="Asthma_NCDM_GIS_Unadjusted_ED_CensusTract", 
        output_layer="Asthma_NCDM_GIS_Unadjusted_ED_CensusTract",
        existing_layer= "MDHEPHT.EPHT.Asthma_NCDM_GIS_Unadjusted_ED_CensusTract",
        expression= f"(TYPE_ID = 18) AND (YEAR = {Asthma.year})")
    
    print("TractAsthma Instance:")
    print(f"Layer Name: {tract_asthma_instance.layer_name}")
    print(f"import_modules: {tract_asthma_instance.import_modules}")
    print(f"allow_overwriting_output: {tract_asthma_instance.allow_overwriting_output}")
    print(f"database_read: {tract_asthma_instance.database_read}")
    print(f"scratch_gdb: {tract_asthma_instance.scratch_gdb}")
    print(f"output_gdb: {tract_asthma_instance.output_gdb}")
    print(f"year: {tract_asthma_instance.year}")
    print(f"geometry: {tract_asthma_instance.geometry}")
    print(f"database_table: {tract_asthma_instance.database_table}")
    print(f"existing_layer: {tract_asthma_instance.existing_layer}")
    print(f"geometry_layer: {tract_asthma_instance.geometry_layer}")
    print(f"expression: {tract_asthma_instance.expression}")
    print(f"input_join_field: {tract_asthma_instance.input_join_field}")
    print(f"target_join_field: {tract_asthma_instance.target_join_field}")
    print(f"output_layer: {tract_asthma_instance.output_layer}")
    print(f"copy_geometry_to_scratch_gdb: {tract_asthma_instance.copy_geometry_to_scratch_gdb}")
    print(f"query_table_from_db_table: {tract_asthma_instance.query_table_from_db_table}")
    print(f"save_query_table_to_scratch_gdb: {tract_asthma_instance.save_query_table_to_scratch_gdb}")
    print(f"join_queried_table_to_geometry: {tract_asthma_instance.join_queried_table_to_geometry}")
    print(f"copy_layer_to_output_gdb: {tract_asthma_instance.copy_layer_to_output_gdb}")
    print(f"delete_rows_from_existing_layer: {tract_asthma_instance.delete_rows_from_existing_layer}")
    print(f"append_queried_table_to_existing_layer: {tract_asthma_instance.append_queried_table_to_existing_layer}")
