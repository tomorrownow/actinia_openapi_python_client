# coding: utf-8

# flake8: noqa

"""
    Actinia

     ================================ Actinia - The GRASS GIS REST API ================================  **Actinia** is an open source REST API for scalable, distributed, high performance processing of geographical data that uses GRASS GIS for computational tasks.  It provides a REST API to process satellite images, time series of satellite images, arbitrary raster data with geographical relations and vector data.  The REST interface allows to access, manage and manipulate the GRASS GIS database via HTTP GET,PUT,POST and DELETE requests and to process raster, vector and time series data located in a persistent GRASS GIS database. **Actinia** allows the processing of cloud based data, for example all Landsat 4-8 scenes as well as all Sentinel2A scenes in an ephemeral databases. The computational results of ephemeral processing are available via object storage as GeoTIFF files.  The full API documentation is available here: https://redocly.github.io/redoc/?url=https://actinia.mundialis.de/latest/ swagger.json   Examples: ---------  To execute the examples, first setup login information, IP address and port:      export ACTINIA_URL=https://actinia.mundialis.de/latest     export AUTH='-u demouser:gu3st!pa55w0rd'  **Data management**  - List all locations that are available in the actinia persistent database:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations\"  - List all mapsets in the location latlong_wgs84:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets\"  - List all raster layers in location latlong_wgs84 and mapset Sentinel2A      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets/Sentinel2A/raster_layers\"  - List all space-time raster datasets (STRDS) in location ECAD and mapset   PERMANENT:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/raster_layers\"  - List all raster map layers of the STRDS precipitation_1950_2013_yearly_mm:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/strds/precipitation_    1950_2013_yearly_mm/raster_layers\"  **Landsat and Sentinel2A NDVI computation**  This API call will compute the NDVI of the top of atmosphere (TOAR) corrected Landsat4 scene LC80440342016259LGN00:      curl ${AUTH} -X POST \"${ACTINIA_URL}/landsat_process/    LC80440342016259LGN00/TOAR/NDVI\"  NDVI computation of Sentinel2A scene S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138:      curl ${AUTH} -X POST \"${ACTINIA_URL}/sentinel2_process/ndvi/    S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138\"  The results of the asynchronous computations are available as GeoTIFF file in a cloud storage for download. 

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.1"

# import apis into sdk package
from actinia_openapi_python_client.api.api_log_api import APILogApi
from actinia_openapi_python_client.api.authentication_management_api import AuthenticationManagementApi
from actinia_openapi_python_client.api.cache_management_api import CacheManagementApi
from actinia_openapi_python_client.api.file_management_api import FileManagementApi
from actinia_openapi_python_client.api.geo_network_api import GeoNetworkApi
from actinia_openapi_python_client.api.location_management_api import LocationManagementApi
from actinia_openapi_python_client.api.mapset_management_api import MapsetManagementApi
from actinia_openapi_python_client.api.mapsets_api import MapsetsApi
from actinia_openapi_python_client.api.merge_api import MergeApi
from actinia_openapi_python_client.api.module_viewer_api import ModuleViewerApi
from actinia_openapi_python_client.api.process_chain_monitoring_api import ProcessChainMonitoringApi
from actinia_openapi_python_client.api.process_chain_template_management_api import ProcessChainTemplateManagementApi
from actinia_openapi_python_client.api.processing_api import ProcessingApi
from actinia_openapi_python_client.api.raster_management_api import RasterManagementApi
from actinia_openapi_python_client.api.raster_sampling_api import RasterSamplingApi
from actinia_openapi_python_client.api.raster_statistics_api import RasterStatisticsApi
from actinia_openapi_python_client.api.resource_iteration_management_api import ResourceIterationManagementApi
from actinia_openapi_python_client.api.resource_management_api import ResourceManagementApi
from actinia_openapi_python_client.api.stac_api import STACApi
from actinia_openapi_python_client.api.strds_management_api import STRDSManagementApi
from actinia_openapi_python_client.api.strds_sampling_api import STRDSSamplingApi
from actinia_openapi_python_client.api.strds_statistics_api import STRDSStatisticsApi
from actinia_openapi_python_client.api.satellite_image_algorithms_api import SatelliteImageAlgorithmsApi
from actinia_openapi_python_client.api.tiling_api import TilingApi
from actinia_openapi_python_client.api.user_management_api import UserManagementApi
from actinia_openapi_python_client.api.vector_management_api import VectorManagementApi
from actinia_openapi_python_client.api.vector_sampling_api import VectorSamplingApi

# import ApiClient
from actinia_openapi_python_client.api_response import ApiResponse
from actinia_openapi_python_client.api_client import ApiClient
from actinia_openapi_python_client.configuration import Configuration
from actinia_openapi_python_client.exceptions import OpenApiException
from actinia_openapi_python_client.exceptions import ApiTypeError
from actinia_openapi_python_client.exceptions import ApiValueError
from actinia_openapi_python_client.exceptions import ApiKeyError
from actinia_openapi_python_client.exceptions import ApiAttributeError
from actinia_openapi_python_client.exceptions import ApiException

# import models into sdk package
from actinia_openapi_python_client.models.api_info_model import ApiInfoModel
from actinia_openapi_python_client.models.api_log_entry_model import ApiLogEntryModel
from actinia_openapi_python_client.models.api_log_list_model import ApiLogListModel
from actinia_openapi_python_client.models.area_univar_result_model import AreaUnivarResultModel
from actinia_openapi_python_client.models.band_information_entry import BandInformationEntry
from actinia_openapi_python_client.models.categorical_statistics_result_model import CategoricalStatisticsResultModel
from actinia_openapi_python_client.models.exception_traceback_model import ExceptionTracebackModel
from actinia_openapi_python_client.models.geodata_response_model import GeodataResponseModel
from actinia_openapi_python_client.models.grass_module import GrassModule
from actinia_openapi_python_client.models.grid_tiling_response_model import GridTilingResponseModel
from actinia_openapi_python_client.models.io_parameter_base import IOParameterBase
from actinia_openapi_python_client.models.input_parameter import InputParameter
from actinia_openapi_python_client.models.input_parameter_import_descr import InputParameterImportDescr
from actinia_openapi_python_client.models.landsat_ndvi_response_model import LandsatNDVIResponseModel
from actinia_openapi_python_client.models.landsat_scene_list_model import LandsatSceneListModel
from actinia_openapi_python_client.models.location_list_response_model import LocationListResponseModel
from actinia_openapi_python_client.models.locked_mapset_list_response_model import LockedMapsetListResponseModel
from actinia_openapi_python_client.models.mapset_info_model import MapsetInfoModel
from actinia_openapi_python_client.models.mapset_info_response_model import MapsetInfoResponseModel
from actinia_openapi_python_client.models.mapset_lock_management_response_model import MapsetLockManagementResponseModel
from actinia_openapi_python_client.models.mapset_size_response_model import MapsetSizeResponseModel
from actinia_openapi_python_client.models.max_mapset_size_response_model import MaxMapsetSizeResponseModel
from actinia_openapi_python_client.models.merge_list_response_model import MergeListResponseModel
from actinia_openapi_python_client.models.merge_short_desc_response_model import MergeShortDescResponseModel
from actinia_openapi_python_client.models.module import Module
from actinia_openapi_python_client.models.module_export_description import ModuleExportDescription
from actinia_openapi_python_client.models.module_import_description import ModuleImportDescription
from actinia_openapi_python_client.models.module_list import ModuleList
from actinia_openapi_python_client.models.module_parameter import ModuleParameter
from actinia_openapi_python_client.models.module_parameter_schema import ModuleParameterSchema
from actinia_openapi_python_client.models.module_returns import ModuleReturns
from actinia_openapi_python_client.models.output_parameter import OutputParameter
from actinia_openapi_python_client.models.output_parameter_export import OutputParameterExport
from actinia_openapi_python_client.models.output_parameter_metadata import OutputParameterMetadata
from actinia_openapi_python_client.models.point_list_model import PointListModel
from actinia_openapi_python_client.models.process_chain_model import ProcessChainModel
from actinia_openapi_python_client.models.process_chain_template import ProcessChainTemplate
from actinia_openapi_python_client.models.process_chain_template_template import ProcessChainTemplateTemplate
from actinia_openapi_python_client.models.process_log_model import ProcessLogModel
from actinia_openapi_python_client.models.processing_error_response_model import ProcessingErrorResponseModel
from actinia_openapi_python_client.models.processing_response_list_model import ProcessingResponseListModel
from actinia_openapi_python_client.models.processing_response_model import ProcessingResponseModel
from actinia_openapi_python_client.models.progress_info_model import ProgressInfoModel
from actinia_openapi_python_client.models.projection_info_model import ProjectionInfoModel
from actinia_openapi_python_client.models.raster_area_stats_response_model import RasterAreaStatsResponseModel
from actinia_openapi_python_client.models.raster_area_univar_stats_response_model import RasterAreaUnivarStatsResponseModel
from actinia_openapi_python_client.models.raster_color_model import RasterColorModel
from actinia_openapi_python_client.models.raster_info_model import RasterInfoModel
from actinia_openapi_python_client.models.raster_info_response_model import RasterInfoResponseModel
from actinia_openapi_python_client.models.raster_list_entry_model import RasterListEntryModel
from actinia_openapi_python_client.models.raster_sampling_response_model import RasterSamplingResponseModel
from actinia_openapi_python_client.models.region_model import RegionModel
from actinia_openapi_python_client.models.strds_creation_model import STRDSCreationModel
from actinia_openapi_python_client.models.strds_info_model import STRDSInfoModel
from actinia_openapi_python_client.models.strds_info_response_model import STRDSInfoResponseModel
from actinia_openapi_python_client.models.strds_raster_list_entry_model import STRDSRasterListEntryModel
from actinia_openapi_python_client.models.strds_raster_list_response_model import STRDSRasterListResponseModel
from actinia_openapi_python_client.models.strds_sample_geo_json_response_model import STRDSSampleGeoJSONResponseModel
from actinia_openapi_python_client.models.strds_sample_response_model import STRDSSampleResponseModel
from actinia_openapi_python_client.models.satellite_scene_entry import SatelliteSceneEntry
from actinia_openapi_python_client.models.satellite_scene_list import SatelliteSceneList
from actinia_openapi_python_client.models.sentinel2_a_scene_entry import Sentinel2ASceneEntry
from actinia_openapi_python_client.models.sentinel2_a_scene_list import Sentinel2ASceneList
from actinia_openapi_python_client.models.sentinel2_a_scene_list_model import Sentinel2ASceneListModel
from actinia_openapi_python_client.models.sentinel2_a_tile_entry import Sentinel2ATileEntry
from actinia_openapi_python_client.models.sentinel_ndvi_response_model import SentinelNDVIResponseModel
from actinia_openapi_python_client.models.set_region_model import SetRegionModel
from actinia_openapi_python_client.models.simple_response_model import SimpleResponseModel
from actinia_openapi_python_client.models.simple_status_code_response_model import SimpleStatusCodeResponseModel
from actinia_openapi_python_client.models.stac_collections_post400_response import StacCollectionsPost400Response
from actinia_openapi_python_client.models.stac_collections_post_request import StacCollectionsPostRequest
from actinia_openapi_python_client.models.stac_collections_stac_collection_id_delete400_response import StacCollectionsStacCollectionIdDelete400Response
from actinia_openapi_python_client.models.stac_collections_stac_collection_id_get400_response import StacCollectionsStacCollectionIdGet400Response
from actinia_openapi_python_client.models.stac_instances_post400_response import StacInstancesPost400Response
from actinia_openapi_python_client.models.stac_instances_post_request import StacInstancesPostRequest
from actinia_openapi_python_client.models.stac_instances_stac_instance_id_delete400_response import StacInstancesStacInstanceIdDelete400Response
from actinia_openapi_python_client.models.stac_instances_stac_instance_id_get400_response import StacInstancesStacInstanceIdGet400Response
from actinia_openapi_python_client.models.stdout_parser import StdoutParser
from actinia_openapi_python_client.models.storage_model import StorageModel
from actinia_openapi_python_client.models.storage_response_model import StorageResponseModel
from actinia_openapi_python_client.models.string_list_processing_result_response_model import StringListProcessingResultResponseModel
from actinia_openapi_python_client.models.tiling_list_response_model import TilingListResponseModel
from actinia_openapi_python_client.models.tiling_short_desc_response_model import TilingShortDescResponseModel
from actinia_openapi_python_client.models.token_response_model import TokenResponseModel
from actinia_openapi_python_client.models.univar_result_model import UnivarResultModel
from actinia_openapi_python_client.models.url_model import UrlModel
from actinia_openapi_python_client.models.user_info_response_model import UserInfoResponseModel
from actinia_openapi_python_client.models.user_info_response_model_permissions import UserInfoResponseModelPermissions
from actinia_openapi_python_client.models.user_list_response_model import UserListResponseModel
from actinia_openapi_python_client.models.vector_attribute_model import VectorAttributeModel
from actinia_openapi_python_client.models.vector_creation_model import VectorCreationModel
from actinia_openapi_python_client.models.vector_info_model import VectorInfoModel
from actinia_openapi_python_client.models.vector_info_response_model import VectorInfoResponseModel
from actinia_openapi_python_client.models.vector_region_creation_model import VectorRegionCreationModel
from actinia_openapi_python_client.models.vector_sampling_response_model import VectorSamplingResponseModel
from actinia_openapi_python_client.models.webhooks import Webhooks