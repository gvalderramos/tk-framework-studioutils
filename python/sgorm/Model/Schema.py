import Model
import DataType


class Asset(Model.Entity):
    def __init__(self):
        super(Asset, self).__init__(self.__class__.__name__)

        self.code = DataType.Field("code", None)
        self.image = DataType.Field("image", None)
        self.sg_published_files = DataType.Field("sg_published_files", None)
        self.episodes = DataType.Field("episodes", None)
        self.tasks = DataType.Field("tasks", None)
        self.yeti_x_asset = DataType.Field(
            "custom_entity07_sg_asset_custom_entity07s", None
        )
        self.sequences = DataType.Field("sequences", None)
        self.cached_display_name = DataType.Field("cached_display_name", None)
        self.sg_work_files = DataType.Field("sg_work_files", None)
        self.mocap_takes = DataType.Field("mocap_takes", None)
        self.shots = DataType.Field("shots", None)
        self.task_template = DataType.Field("task_template", None)
        self.parents = DataType.Field("parents", None)
        self.sg_versions = DataType.Field("sg_versions", None)
        self.sg_geometries = DataType.Field("sg_geometries", None)
        self.sg_status_list = DataType.Field("sg_status_list", None)
        self.description = DataType.Field("description", None)
        self.addressings_cc = DataType.Field("addressings_cc", None)
        self.tags = DataType.Field("tags", None)
        self.assets = DataType.Field("assets", None)
        self.sg_keep = DataType.Field("sg_keep", None)
        self.image_source_entity = DataType.Field("image_source_entity", None)
        self.project = DataType.Field("project", None)
        self.filmstrip_image = DataType.Field("filmstrip_image", None)
        self.sg_mocap_status = DataType.Field("sg_mocap_status", None)
        self.sg_vendor_groups = DataType.Field("sg_vendor_groups", None)
        self.sg_asset_type = DataType.Field("sg_asset_type", None)
        self.workfiles_x_assets = DataType.Field(
            "custom_entity04_sg_asset_custom_entity04s", None
        )
