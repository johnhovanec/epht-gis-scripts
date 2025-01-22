class BaseClass:
    def __init__(self, layer_name):
        self.layer_name = layer_name
    database_read = "D:/MDH//Connections2/MDH DEV mdhephtdbdev1 to _MDHEPHT_ via READ.sde"
    import_modules = "import arcpy from sys import argv"
    allow_overwriting_output = "print('I am jelly donut')" # use eval to run strings as code

    # Factory method function
    @staticmethod
    def construct_instance(config_name):
        """
        Construct an instance of the appropriate class based on the configuration name.
        """
        config = CONFIGURATIONS.get(config_name)
        if not config:
            raise ValueError(f"Configuration '{config_name}' not found.")

        return CommonLayer(**config)


class CommonLayer(BaseClass):
    def __init__(self, layer_name, year, geometry, database_table, geometry_layer, output_layer, copy_geometry_to_scratch_gdb, query_table_from_db_table):
        """
        Initialize CommonLayer with layer_name, year, and geometry.
        """
        super().__init__(layer_name)  # Initialize BaseClass
        self.year = year
        self.geometry = geometry
        self.database_table = database_table
        self.geometry_layer = geometry_layer
        self.output_layer = output_layer
        self.copy_geometry_to_scratch_gdb = copy_geometry_to_scratch_gdb
        self.query_table_from_db_table = query_table_from_db_table

    def copy_geo(self, source, destination):
        """
        Simulate copying geographical data from source to destination.
        """
        print("In copy geo")

YEAR_CONFIG = {"year": 2025}

COMMON_LAYER_CONFIG = {"database_table": "database_read + 'MDHEPHT.epht.Asthma_NCDM_' + geometry",
                       "copy_geometry_to_scratch_gdb": "arcpy.management.CopyFeatures({geometry_layer}, scratch_gdb + 'Copied_Geometry')",
                        "query_table_from_db_table": "arcpy.management.MakeQueryTable(database_table, 'Query_Table')" }

COMMON_COUNTY_LAYER_CONFIG = {"geometry": "County", "geometry_layer": "MDHEPHT.EPHT.GIS_County_Poly", **COMMON_LAYER_CONFIG, **YEAR_CONFIG}

COMMON_CENSUS_TRACT_LAYER_CONFIG = {"geometry": "CensusTract", "geometry_layer": "MDHEPHT.EPHT.GIS_CensusTract20_Poly", **COMMON_LAYER_CONFIG, **YEAR_CONFIG}

CONFIGURATIONS = {
    "Asthma_NCDM_GIS_AgeAdjusted_ED_County": {
        "layer_name": "Asthma_NCDM_GIS_AgeAdjusted_ED_County", 
        "output_layer": "Asthma_NCDM_GIS_AgeAdjusted_ED_County", 
        **COMMON_COUNTY_LAYER_CONFIG},
    "Asthma_NCDM_GIS_Unadjusted_ED_County": {
        "layer_name": "Asthma_NCDM_GIS_Unadjusted_ED_County", 
        "output_layer": "Asthma_NCDM_GIS_Unadjusted_ED_County", 
        **COMMON_COUNTY_LAYER_CONFIG},
    "Asthma_NCDM_GIS_Unadjusted_ED_CensusTract": {
        "layer_name": "Asthma_NCDM_GIS_Unadjusted_ED_CensusTract", 
        "output_layer": "Asthma_NCDM_GIS_Unadjusted_ED_CensusTract", 
        **COMMON_CENSUS_TRACT_LAYER_CONFIG},
}



# Example usage
# Construct instances based on configurations
county_age_adjusted = BaseClass.construct_instance("Asthma_NCDM_GIS_AgeAdjusted_ED_County")
print(county_age_adjusted.year, county_age_adjusted.import_modules, county_age_adjusted.geometry, county_age_adjusted.layer_name, county_age_adjusted.output_layer, county_age_adjusted.copy_geometry_to_scratch_gdb)

county_unadjusted = BaseClass.construct_instance("Asthma_NCDM_GIS_Unadjusted_ED_County")
print(county_unadjusted.year, county_age_adjusted.import_modules, county_unadjusted.geometry, county_unadjusted.layer_name, county_unadjusted.output_layer, county_unadjusted.copy_geometry_to_scratch_gdb)

tract_unadjusted = BaseClass.construct_instance("Asthma_NCDM_GIS_Unadjusted_ED_CensusTract")
print(county_age_adjusted.year, county_age_adjusted.import_modules, tract_unadjusted.geometry, tract_unadjusted.layer_name, tract_unadjusted.output_layer, tract_unadjusted.copy_geometry_to_scratch_gdb)
