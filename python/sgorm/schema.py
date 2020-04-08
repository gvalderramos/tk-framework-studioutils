from . import model
from . import datatype


class Asset(model.Entity):
    def __init__(self):
        super(Asset, self).__init__(self.__class__.__name__)

        self.code = datatype.Field("code", None)
        self.image = datatype.Field("image", None)
        self.sg_published_files = datatype.Field("sg_published_files", None)
        self.episodes = datatype.Field("episodes", None)
        self.tasks = datatype.Field("tasks", None)
        self.yeti_x_asset = datatype.Field(
            "custom_entity07_sg_asset_custom_entity07s", None
        )
        self.sequences = datatype.Field("sequences", None)
        self.cached_display_name = datatype.Field("cached_display_name", None)
        self.sg_work_files = datatype.Field("sg_work_files", None)
        self.mocap_takes = datatype.Field("mocap_takes", None)
        self.shots = datatype.Field("shots", None)
        self.task_template = datatype.Field("task_template", None)
        self.parents = datatype.Field("parents", None)
        self.sg_versions = datatype.Field("sg_versions", None)
        self.sg_geometries = datatype.Field("sg_geometries", None)
        self.sg_status_list = datatype.Field("sg_status_list", None)
        self.description = datatype.Field("description", None)
        self.addressings_cc = datatype.Field("addressings_cc", None)
        self.tags = datatype.Field("tags", None)
        self.assets = datatype.Field("assets", None)
        self.sg_keep = datatype.Field("sg_keep", None)
        self.image_source_entity = datatype.Field("image_source_entity", None)
        self.project = datatype.Field("project", None)
        self.filmstrip_image = datatype.Field("filmstrip_image", None)
        self.sg_mocap_status = datatype.Field("sg_mocap_status", None)
        self.sg_vendor_groups = datatype.Field("sg_vendor_groups", None)
        self.sg_asset_type = datatype.Field("sg_asset_type", None)
        self.workfiles_x_assets = datatype.Field(
            "custom_entity04_sg_asset_custom_entity04s", None
        )
