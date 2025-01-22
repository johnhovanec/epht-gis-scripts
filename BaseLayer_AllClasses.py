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
    def __init__(self, layer_name, year, geometry, database_table, existing_layer, geometry_layer, output_layer, copy_geometry_to_scratch_gdb, query_table_from_db_table):
        """
        Initialize CommonLayer with all its attributes.
        """
        super().__init__(layer_name)
        self.year = year
        self.geometry = geometry
        self.database_table = database_table
        self.existing_layer = existing_layer
        self.geometry_layer = geometry_layer
        self.output_layer = output_layer
        self.copy_geometry_to_scratch_gdb = copy_geometry_to_scratch_gdb
        self.query_table_from_db_table = query_table_from_db_table

    def copy_geo(self, source, destination):
        """
        Simulate copying geographical data from source to destination.
        """
        print(f"Copying data from {source} to {destination}.")


class Asthma(CommonLayer):
    def __init__(self, layer_name, output_layer, geometry, geometry_layer, existing_layer):
        """
        Initialize Asthma with its specific attributes.
        """
        database_table = f"{self.database_read} + 'MDHEPHT.epht.Asthma_NCDM_' + {geometry}"
        existing_layer = f"{self.database_read} + {existing_layer}"
        copy_geometry_to_scratch_gdb = f"{self.copied_geometry} = arcpy.management.CopyFeatures({geometry_layer}, {self.scratch_gdb} + 'Copied_Geometry')"
        query_table_from_db_table = f"arcpy.management.MakeQueryTable({database_table}, 'Query_Table')"
        super().__init__(layer_name, self.year, geometry, database_table, existing_layer, geometry_layer, output_layer, copy_geometry_to_scratch_gdb, query_table_from_db_table)

    # Properties that are common to all instances for Asthma
    year = 2025
    copied_geometry = None  # Placeholder for dynamically created variable that will need to be set to result of copy_geometry_to_scratch_gdb
    query_table = None  # Placeholder for dynamically created variable that will need to be set to result of query_table_from_db_table
    queried_table = None  # Placeholder for dynamically created variable that will need to be set to result of save_query_table_to_scratch_gdb
    geometry_with_join = None  # Placeholder for dynamically created variable that will need to be set to result of join_queried_table_to_geometry
    copied_layer = None  # Placeholder for dynamically created variable that will need to be set to result of copy_layer_to_output_gdb
    empty_layer = None  # Placeholder for dynamically created variable that will need to be set to result of delete_rows_from_existing_layer

class AsthmaCounty(Asthma):
    _geometry = "County"
    _geometry_layer = "MDHEPHT.EPHT.GIS_County_Poly"

    def __init__(self, layer_name, output_layer, existing_layer):
        """
        Initialize CountyAsthma with its specific attributes.
        """
        super().__init__(layer_name, output_layer, self._geometry, self._geometry_layer, existing_layer)


class AsthmaCensusTract(Asthma):
    _geometry = "CensusTract"
    _geometry_layer = "MDHEPHT.EPHT.GIS_CensusTract20_Poly"

    def __init__(self, layer_name, output_layer, existing_layer):
        """
        Initialize CensusTractAsthma with its specific attributes.
        """
        super().__init__(layer_name, output_layer, self._geometry, self._geometry_layer, existing_layer,)


# Example usage
if __name__ == "__main__":
    # Create an instance of AsthmaCounty
    county_asthma_instance = AsthmaCounty(
        layer_name="Asthma_NCDM_GIS_AgeAdjusted_ED_County", 
        # expression= "(TYPE_ID = 17) AND (year = year) AND (GROUPAGE_ID = 8)",
        output_layer="Asthma_NCDM_GIS_AgeAdjusted_ED_County",
        existing_layer= "MDHEPHT.EPHT.Asthma_NCDM_GIS_AgeAdjusted_ED_County")
    
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
    print(f"output_layer: {county_asthma_instance.output_layer}")
    print(f"Copy Geometry to scratch_gdb: {county_asthma_instance.copy_geometry_to_scratch_gdb}")
    print(f"Query Table from DB Table: {county_asthma_instance.query_table_from_db_table}")

    print("\n")

    # Create an instance of AsthmaCounty
    county_unadjusted_asthma_instance = AsthmaCounty(
        layer_name="Asthma_NCDM_GIS_Unadjusted_ED_County", 
        output_layer="Asthma_NCDM_GIS_Unadjusted_ED_County",
        existing_layer="MDHEPHT.EPHT.Asthma_NCDM_GIS_Unadjusted_ED_County")
    
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
    print(f"output_layer: {county_unadjusted_asthma_instance.output_layer}")
    print(f"Copy Geometry to Scratch GDB: {county_unadjusted_asthma_instance.copy_geometry_to_scratch_gdb}")
    print(f"Query Table from DB Table: {county_unadjusted_asthma_instance.query_table_from_db_table}")

    print("\n")

    #  # Create an instance of CensusTractAsthma
    tract_asthma_instance = AsthmaCensusTract(
        layer_name="Asthma_NCDM_GIS_Unadjusted_ED_CensusTract", 
        output_layer="Asthma_NCDM_GIS_Unadjusted_ED_CensusTract",
        existing_layer= "MDHEPHT.EPHT.Asthma_NCDM_GIS_Unadjust ed_ED_CensusTract")
    
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
    print(f"output_layer: {tract_asthma_instance.output_layer}")
    print(f"Copy Geometry to Scratch GDB: {tract_asthma_instance.copy_geometry_to_scratch_gdb}")
    print(f"Query Table from DB Table: {tract_asthma_instance.query_table_from_db_table}")





# Complex one

# class BaseLayer:
#     def __init__(self, layer_name):
#         """
#         Initialize BaseClass with layer_name.
#         """
#         self.layer_name = layer_name
    
#     # Properties that are common to all instances 
#     import_modules = "import arcpy from sys import argv"
#     allow_overwriting_output = f"arcpy.env.overwriteOutput = {True}"
#     database_read = "D:/MDH//Connections2/MDH DEV mdhephtdbdev1 to _MDHEPHT_ via READ.sde"
#     scratch_gdb = ".../mdh-epht-gis-utilities/WorkingDocument/Scratch.gdb"
#     output_gdb = ".../mdh-epht-gis-utilities/WorkingDocument/Outputs.gdb"


# class CommonLayer(BaseLayer):
#     def __init__(self, layer_name, year, geometry, database_table, existing_layer, geometry_layer, expression, 
#                 #  input_join_field, target_join_field, 
#                 output_layer, copy_geometry_to_scratch_gdb, query_table_from_db_table
#                 #  save_query_table_to_scratch_gdb, join_queried_table_to_geometry, copy_layer_to_output_gdb, 
#                 #  delete_rows_from_existing_layer, append_queried_table_to_existing_layer
#                  ):
#         """
#         Initialize CommonLayer with all its attributes.
#         """
#         super().__init__(layer_name)
#         self.year = year
#         self.geometry = geometry
#         self.database_table = database_table
#         self.existing_layer = existing_layer
#         self.geometry_layer = geometry_layer
#         self.expression = expression
#         # self.input_join_field = input_join_field
#         # self.target_join_field = target_join_field
#         self.output_layer = output_layer
#         self.copy_geometry_to_scratch_gdb = copy_geometry_to_scratch_gdb
#         self.query_table_from_db_table = query_table_from_db_table
#         # self.save_query_table_to_scratch_gdb = save_query_table_to_scratch_gdb
#         # self.join_queried_table_to_geometry = join_queried_table_to_geometry
#         # self.copy_layer_to_output_gdb = copy_layer_to_output_gdb
#         # self.delete_rows_from_existing_layer = delete_rows_from_existing_layer
#         # self.append_queried_table_to_existing_layer = append_queried_table_to_existing_layer



#     def copy_geo(self, source, destination):
#         """
#         Simulate copying geographical data from source to destination.
#         """
#         print(f"Copying data from {source} to {destination}.")


# class Asthma(CommonLayer):
#     _year = 2025

#     def __init__(self, layer_name, database_read, output_layer, geometry, geometry_layer, existing_layer, scratch_gdb, 
#                  expression
#                 #  input_join_field, target_join_field, copied_geometry, query_table, queried_table, 
#                 #  geometry_with_join, copied_layer, empty_layer
#                 ):
#         """
#         Initialize Asthma with its specific attributes.
#         """
#         database_table = f"{database_read} + 'MDHEPHT.epht.Asthma_NCDM_' + {geometry}"
#         copy_geometry_to_scratch_gdb = f"arcpy.management.CopyFeatures({geometry_layer}, {scratch_gdb} + 'Copied_Geometry')"
#         query_table_from_db_table = f"{self.query_table} = arcpy.management.MakeQueryTable({database_table}, 'Query_Table')"
#         save_query_table_to_scratch_gdb = f"arcpy.conversion.TableToTable({query_table}, {scratch_gdb}, 'Queried_Table', {expression})"
#         super().__init__(layer_name, self._year, geometry, database_table, existing_layer, geometry_layer, expression, 
#                     output_layer, copy_geometry_to_scratch_gdb, query_table_from_db_table, 
#                     save_query_table_to_scratch_gdb
#                     # join_queried_table_to_geometry, copy_layer_to_output_gdb, 
#                     # delete_rows_from_existing_layer, append_queried_table_to_existing_layer
#                     )

#         self.copied_geometry = None  # Placeholder for dynamically created variable
#         self.query_table = None  # Placeholder for dynamically created variable
#         self.queried_table = None  # Placeholder for dynamically created variable
#         self.geometry_with_join = None  # Placeholder for dynamically created variable
#         self.copied_layer = None  # Placeholder for dynamically created variable
#         self.empty_layer = None  # Placeholder for dynamically created variable
   


# class AsthmaCounty(Asthma):
#     _geometry = "County"
#     _geometry_layer = "MDHEPHT.EPHT.GIS_County_Poly"

#     def __init__(self, layer_name, output_layer, expression, existing_layer, scratch_gdb,):
#         """
#         Initialize CountyAsthma with its specific attributes.
#         """
#         super().__init__(layer_name, output_layer, expression, existing_layer, scratch_gdb, self._geometry, self._geometry_layer)


# class AsthmaCensusTract(Asthma):
#     _geometry = "CensusTract"
#     _geometry_layer = "MDHEPHT.EPHT.GIS_CensusTract20_Poly"

#     def __init__(self, layer_name, output_layer):
#         """
#         Initialize CensusTractAsthma with its specific attributes.
#         """
#         super().__init__(layer_name, output_layer, self._geometry, self._geometry_layer)


# # Example usage
# if __name__ == "__main__":
   
#     # Create an instance of CountyAsthma
#     county_asthma_instance = AsthmaCounty(
#         layer_name="Asthma_NCDM_GIS_AgeAdjusted_ED_County", 
#         existing_layer= f"{database_read} + 'MDHEPHT.EPHT.Asthma_NCDM_GIS_AgeAdjusted_ED_County'"
#         expression= "(TYPE_ID = 17) AND (year = year) AND (GROUPAGE_ID = 8)",
#         output_layer="Asthma_NCDM_GIS_AgeAdjusted_ED_County")
    
#     print("CountyAsthma Instance:")
#     print(f"import_modules: {county_asthma_instance.import_modules}")
#     print(f"allow_overwriting_output: {county_asthma_instance.allow_overwriting_output}")
#     print(f"database_read: {county_asthma_instance.database_read}")
#     print(f"scratch_gdb: {county_asthma_instance.scratch_gdb}")
#     print(f"output_gdb: {county_asthma_instance.output_gdb}")
#     print(f"Layer Name: {county_asthma_instance.layer_name}")
#     print(f"year: {county_asthma_instance.year}")
#     print(f"Geometry: {county_asthma_instance.geometry}")
#     print(f"database_table: {county_asthma_instance.database_table}")
#     print(f"geometry_layer: {county_asthma_instance.geometry_layer}")
#     print(f"output_layer: {county_asthma_instance.output_layer}")
#     print(f"Copy Geometry to Scratch GDB: {county_asthma_instance.copy_geometry_to_scratch_gdb}")
#     print(f"Query Table from DB Table: {county_asthma_instance.query_table_from_db_table}")


#     print("\n")

#     # Create an instance of CountyAsthma
#     county_unadjusted_asthma_instance = AsthmaCounty(layer_name="Asthma_NCDM_GIS_Unadjusted_ED_County", output_layer="Asthma_NCDM_GIS_Unadjusted_ED_County")
    
#     print("CountyAsthma Instance 2:")
#     print(f"import_modules: {county_unadjusted_asthma_instance.import_modules}")
#     print(f"allow_overwriting_output: {county_unadjusted_asthma_instance.allow_overwriting_output}")
#     print(f"database_read: {county_unadjusted_asthma_instance.database_read}")
#     print(f"scratch_gdb: {county_unadjusted_asthma_instance.scratch_gdb}")
#     print(f"output_gdb: {county_unadjusted_asthma_instance.output_gdb}")
#     print(f"Layer Name: {county_unadjusted_asthma_instance.layer_name}")
#     print(f"year: {county_unadjusted_asthma_instance.year}")
#     print(f"Geometry: {county_unadjusted_asthma_instance.geometry}")
#     print(f"database_table: {county_unadjusted_asthma_instance.database_table}")
#     print(f"geometry_layer: {county_unadjusted_asthma_instance.geometry_layer}")
#     print(f"output_layer: {county_unadjusted_asthma_instance.output_layer}")
#     print(f"Copy Geometry to Scratch GDB: {county_unadjusted_asthma_instance.copy_geometry_to_scratch_gdb}")
#     print(f"Query Table from DB Table: {county_unadjusted_asthma_instance.query_table_from_db_table}")
    


#     print("\n")

#      # Create an instance of CensusTractAsthma
#     tract_asthma_instance = AsthmaCensusTract(layer_name="Asthma_NCDM_GIS_Unadjusted_ED_CensusTract", output_layer="Asthma_NCDM_GIS_Unadjusted_ED_CensusTract")
    
#     print("CountyAsthma Instance:")
#     print(f"import_modules: {tract_asthma_instance.import_modules}")
#     print(f"allow_overwriting_output: {tract_asthma_instance.allow_overwriting_output}")
#     print(f"database_read: {tract_asthma_instance.database_read}")
#     print(f"output_gdb: {tract_asthma_instance.output_gdb}")
#     print(f"scratch_gdb: {tract_asthma_instance.scratch_gdb}")
#     print(f"Layer Name: {tract_asthma_instance.layer_name}")
#     print(f"year: {tract_asthma_instance.year}")
#     print(f"Geometry: {tract_asthma_instance.geometry}")
#     print(f"database_table: {tract_asthma_instance.database_table}")
#     print(f"geometry_layer: {tract_asthma_instance.geometry_layer}")
#     print(f"output_layer: {tract_asthma_instance.output_layer}")
#     print(f"Copy Geometry to Scratch GDB: {tract_asthma_instance.copy_geometry_to_scratch_gdb}")
#     print(f"Query Table from DB Table: {tract_asthma_instance.query_table_from_db_table}")

