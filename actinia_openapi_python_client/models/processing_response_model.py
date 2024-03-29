# coding: utf-8

"""
    Actinia

     ================================ Actinia - The GRASS GIS REST API ================================  **Actinia** is an open source REST API for scalable, distributed, high performance processing of geographical data that uses GRASS GIS for computational tasks.  It provides a REST API to process satellite images, time series of satellite images, arbitrary raster data with geographical relations and vector data.  The REST interface allows to access, manage and manipulate the GRASS GIS database via HTTP GET,PUT,POST and DELETE requests and to process raster, vector and time series data located in a persistent GRASS GIS database. **Actinia** allows the processing of cloud based data, for example all Landsat 4-8 scenes as well as all Sentinel2A scenes in an ephemeral databases. The computational results of ephemeral processing are available via object storage as GeoTIFF files.  The full API documentation is available here: https://redocly.github.io/redoc/?url=https://actinia.mundialis.de/latest/ swagger.json   Examples: ---------  To execute the examples, first setup login information, IP address and port:      export ACTINIA_URL=https://actinia.mundialis.de/latest     export AUTH='-u demouser:gu3st!pa55w0rd'  **Data management**  - List all locations that are available in the actinia persistent database:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations\"  - List all mapsets in the location latlong_wgs84:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets\"  - List all raster layers in location latlong_wgs84 and mapset Sentinel2A      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets/Sentinel2A/raster_layers\"  - List all space-time raster datasets (STRDS) in location ECAD and mapset   PERMANENT:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/raster_layers\"  - List all raster map layers of the STRDS precipitation_1950_2013_yearly_mm:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/strds/precipitation_    1950_2013_yearly_mm/raster_layers\"  **Landsat and Sentinel2A NDVI computation**  This API call will compute the NDVI of the top of atmosphere (TOAR) corrected Landsat4 scene LC80440342016259LGN00:      curl ${AUTH} -X POST \"${ACTINIA_URL}/landsat_process/    LC80440342016259LGN00/TOAR/NDVI\"  NDVI computation of Sentinel2A scene S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138:      curl ${AUTH} -X POST \"${ACTINIA_URL}/sentinel2_process/ndvi/    S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138\"  The results of the asynchronous computations are available as GeoTIFF file in a cloud storage for download. 

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from actinia_openapi_python_client.models.api_info_model import ApiInfoModel
from actinia_openapi_python_client.models.exception_traceback_model import ExceptionTracebackModel
from actinia_openapi_python_client.models.grass_module import GrassModule
from actinia_openapi_python_client.models.process_log_model import ProcessLogModel
from actinia_openapi_python_client.models.progress_info_model import ProgressInfoModel
from actinia_openapi_python_client.models.url_model import UrlModel
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProcessingResponseModel(BaseModel):
    """
    This is the base class for ALL response models.
    """ # noqa: E501
    status: StrictStr = Field(description="The status of the response")
    user_id: StrictStr = Field(description="The id of the user that issued a request")
    resource_id: StrictStr = Field(description="The unique resource id")
    queue: Optional[StrictStr] = Field(default=None, description="The name of the queue in which the job is queued")
    process_log: Optional[List[ProcessLogModel]] = Field(default=None, description="A list of ProcessLogModels")
    process_chain_list: Optional[List[GrassModule]] = Field(default=None, description="The list of GRASS modules that were used in the processing", min_items=0)
    process_results: Optional[Union[StrictStr, Dict]] = Field(default=None, description="An arbitrary class that stores the processing results")
    progress: Optional[ProgressInfoModel] = None
    message: StrictStr = Field(description="Message for the user, maybe status, finished or error message")
    exception: Optional[ExceptionTracebackModel] = None
    accept_timestamp: Union[StrictFloat, StrictInt] = Field(description="The acceptance timestamp in seconds of the response")
    accept_datetime: StrictStr = Field(description="The acceptance timestamp of the response in human readable format")
    timestamp: Union[StrictFloat, StrictInt] = Field(description="The current timestamp in seconds of the response")
    time_delta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The time delta of the processing in seconds")
    datetime: StrictStr = Field(description="The current timestamp of the response in human readable format")
    http_code: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The HTTP code of the response")
    urls: Optional[UrlModel] = None
    api_info: Optional[ApiInfoModel] = None
    __properties: ClassVar[List[str]] = ["status", "user_id", "resource_id", "queue", "process_log", "process_chain_list", "process_results", "progress", "message", "exception", "accept_timestamp", "accept_datetime", "timestamp", "time_delta", "datetime", "http_code", "urls", "api_info"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProcessingResponseModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in process_log (list)
        _items = []
        if self.process_log:
            for _item in self.process_log:
                if _item:
                    _items.append(_item.to_dict())
            _dict['process_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in process_chain_list (list)
        _items = []
        if self.process_chain_list:
            for _item in self.process_chain_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['process_chain_list'] = _items
        # override the default output from pydantic by calling `to_dict()` of progress
        if self.progress:
            _dict['progress'] = self.progress.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exception
        if self.exception:
            _dict['exception'] = self.exception.to_dict()
        # override the default output from pydantic by calling `to_dict()` of urls
        if self.urls:
            _dict['urls'] = self.urls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of api_info
        if self.api_info:
            _dict['api_info'] = self.api_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProcessingResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "user_id": obj.get("user_id"),
            "resource_id": obj.get("resource_id"),
            "queue": obj.get("queue"),
            "process_log": [ProcessLogModel.from_dict(_item) for _item in obj.get("process_log")] if obj.get("process_log") is not None else None,
            "process_chain_list": [GrassModule.from_dict(_item) for _item in obj.get("process_chain_list")] if obj.get("process_chain_list") is not None else None,
            "process_results": obj.get("process_results"),
            "progress": ProgressInfoModel.from_dict(obj.get("progress")) if obj.get("progress") is not None else None,
            "message": obj.get("message"),
            "exception": ExceptionTracebackModel.from_dict(obj.get("exception")) if obj.get("exception") is not None else None,
            "accept_timestamp": obj.get("accept_timestamp"),
            "accept_datetime": obj.get("accept_datetime"),
            "timestamp": obj.get("timestamp"),
            "time_delta": obj.get("time_delta"),
            "datetime": obj.get("datetime"),
            "http_code": obj.get("http_code"),
            "urls": UrlModel.from_dict(obj.get("urls")) if obj.get("urls") is not None else None,
            "api_info": ApiInfoModel.from_dict(obj.get("api_info")) if obj.get("api_info") is not None else None
        })
        return _obj


