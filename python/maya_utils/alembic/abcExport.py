__all__ = "AbcExport"


class AbcExport(object):
    _args = (_prs, _duf, _v, _j) = ("-prs", "-duf", "-v", "-j")

    class Job(object):
        _args = (
            _a,
            _as,
            _atp,
            _df,
            _ef,
            _f,
            _fr,
            _frs,
            _nn,
            _pr,
            _ro,
            _rt,
            _s,
            _sl,
            _sn,
            _u,
            _uatp,
            _uv,
            _uvo,
            _wcs,
            _wfs,
            _wfg,
            _ws,
            _wv,
            _wuvs,
            _mfc,
            _mpc,
            _pfc,
            _ppc,
        ) = (
            "-a",
            "-as",
            "-atp",
            "-df",
            "-ef",
            "-f",
            "-fr",
            "-frs",
            "-nn",
            "-pr",
            "-ro",
            "-rt",
            "-s",
            "-sl",
            "-sn",
            "-u",
            "-uatp",
            "-uv",
            "-uvo",
            "-wcs",
            "-wfs",
            "-wfg",
            "-ws",
            "-wv",
            "-wuvs",
            "-mfc",
            "-mpc",
            "-pfc",
            "ppc",
        )

        def __init__(
            self,
            attr=None,
            auto_subd=None,
            attr_prefix=None,
            data_format=None,
            euler_filter=None,
            file=None,
            frame_range=None,
            frame_relative_sample=None,
            no_normals=None,
            pre_rool=None,
            renderable_only=None,
            root=None,
            step=None,
            selection=None,
            strip_namespace=None,
            user_attr=None,
            user_attr_prefix=None,
            uv_write=None,
            uvs_only=None,
            write_color_sets=None,
            write_visibility=None,
            whole_frame_geo=None,
            world_space=None,
            write_uv_sets=None,
            write_face_sets=None,
            mel_per_frame_callback=None,
            mel_post_job_callback=None,
            python_per_frame_callback=None,
            python_post_job_callback=None,
        ):
            self._attr = attr if attr else []
            self._auto_subd = auto_subd
            self._attr_prefix = attr_prefix
            self._data_format = data_format
            self._euler_filter = euler_filter
            self._file = file
            self._frame_range = frame_range
            self._frame_relative_sample = frame_relative_sample
            self._no_normals = no_normals
            self._pre_rool = pre_rool
            self._renderable_only = renderable_only
            self._root = root if root else []
            self._step = step
            self._selection = selection
            self._strip_namespace = strip_namespace
            self._user_attr = user_attr
            self._user_attr_prefix = user_attr_prefix if user_attr_prefix else []
            self._uv_write = uv_write
            self._uvs_only = uvs_only
            self._write_color_sets = write_color_sets
            self._write_face_sets = write_face_sets
            self._whole_frame_geo = whole_frame_geo
            self._write_visibility = write_visibility
            self._world_space = world_space
            self._write_visibility = write_visibility
            self._write_uv_sets = write_uv_sets
            self._mel_per_frame_callback = mel_per_frame_callback
            self._mel_post_job_callback = mel_post_job_callback
            self._python_per_frame_callback = python_per_frame_callback
            self._python_post_job_callback = python_post_job_callback

            self.cmd = lambda: "".join(
                [self.attr, self.auto_subd, self.attr_prefix, self.data_format]
            )

        @staticmethod
        def _arg_with_value(key, value):
            if not value:
                return ""

            if isinstance(value, list) or isinstance(value, tuple):
                return " ".join(["{} {}".format(key, v) for v in value])

            return "{} {} ".format(key, value)

        @staticmethod
        def _arg_without_value(key, value):
            if not value:
                return ""

            return "{} ".format(key)

        @property
        def attr(self):
            """
            A specific geometric attribute to write out. This flag may occur more than once.

            :getter: Returns attr parameter
            """

            return self._arg_with_value(self._a, self._attr)

        @attr.setter
        def attr(self, value):
            if not isinstance(value, list) or not isinstance(value, tuple):
                value = [value]

            self._attr = value

        def add_attr(self, *attributes):
            """
            Add attributes

            :param `*attributes`: list of attributes you wount to add
            :type `*attributes`: str
            """
            for attr in attributes:
                self._attr.append(attr)

        @property
        def auto_subd(self):
            return self._arg_without_value(self._as, self._auto_subd)

        @auto_subd.setter
        def auto_subd(self, value):
            self._auto_subd = True if value else False

        @property
        def attr_prefix(self):
            return self._arg_with_value(self._atp, self._attr_prefix)

        @attr_prefix.setter
        def attr_prefix(self, value):
            if not isinstance(value, str):
                value = str(value)
            self._attr_prefix = value

        @property
        def data_format(self):
            return self._arg_with_value(self._df, self._data_format)

        @data_format.setter
        def data_format(self, value):
            if not isinstance(value, str):
                value = str(value)
            self._data_format = value

        @property
        def euler_filter(self):
            return self._arg_without_value(self._ef, self._euler_filter)

        @euler_filter.setter
        def euler_filter(self, value):
            self._euler_filter = True if value else False

        @property
        def file(self):
            return self._arg_with_value(self._f, self._file)

        @file.setter
        def file(self, value):
            self._file = value

        @property
        def frame_relative_sample(self):
            return self._arg_with_value(self._frs, self._frame_relative_sample)

        @frame_relative_sample.setter
        def frame_relative_sample(self, value):
            self._frame_relative_sample = float(value)

        @property
        def no_normals(self):
            return self._arg_without_value(self._nn, self._no_normals)

        @no_normals.setter
        def no_normals(self, value):
            self._no_normals = True if value else False

        @property
        def pre_rool(self):
            return self._arg_without_value(self._pr, self._pre_rool)

        @pre_rool.setter
        def pre_rool(self, value):
            self._pre_rool = True if value else False

        @property
        def renderable_only(self):
            return self._arg_without_value(self._ro, self._renderable_only)

        @renderable_only.setter
        def renderable_only(self, value):
            self._renderable_only = True if value else False

        @property
        def root(self):
            return self._arg_with_value(self._rt, self._root)

        @root.setter
        def root(self, value):
            self._root = value if isinstance(value, list) else [value]

        def add_root(self, *roots):
            for root in roots:
                self._root.append(root)

        @property
        def step(self):
            return self._arg_with_value(self._s, self._step)

        @step.setter
        def step(self, value):
            self._step = float(value)

        @property
        def selection(self):
            return self._arg_without_value(self._sl, self._selection)

        @selection.setter
        def selection(self, value):
            self._selection = True if value else False

        @property
        def strip_namespaces(self):
            return self._arg_with_value(self._sn, self._strip_namespace)

        @strip_namespaces.setter
        def strip_namespaces(self, value):
            self._strip_namespace = int(value)

        @property
        def user_attr(self):
            return self._arg_with_value(self._u, self._user_attr)

        @user_attr.setter
        def user_attr(self, value):
            self._user_attr = value

        @property
        def user_attr_prefix(self):
            return self._arg_with_value(self._uatp, self._user_attr_prefix)

        @user_attr_prefix.setter
        def user_attr_prefix(self, value):
            self._user_attr_prefix = value

        def add_user_attr_prefix(self, *attributes):
            for attr in attributes:
                self._user_attr_prefix.append(attr)

        @property
        def uv_write(self):
            return self._arg_without_value(self._uv, self._uv_write)

        @uv_write.setter
        def uv_write(self, value):
            self._uv_write = True if value else False

        @property
        def write_color_sets(self):
            return self._arg_without_value(self._wcs, self._write_color_sets)

        @write_color_sets.setter
        def write_color_sets(self, value):
            self._write_color_sets = True if value else False

        @property
        def write_face_sets(self):
            return self._arg_without_value(self._wfs, self._write_face_sets)

        @write_face_sets.setter
        def write_face_sets(self, value):
            self._write_face_sets = True if value else False

        @property
        def whole_frame_geo(self):
            return self._arg_without_value(self._wfg, self._whole_frame_geo)

        @whole_frame_geo.setter
        def whole_frame_geo(self, value):
            self._whole_frame_geo = True if value else False

        @property
        def world_space(self):
            return self._arg_without_value(self._ws, self._world_space)

        @world_space.setter
        def world_space(self, value):
            self._world_space = True if value else False

        @property
        def write_visibility(self):
            return self._arg_without_value(self._wv, self._write_visibility)

        @write_visibility.setter
        def write_visibility(self, value):
            self._write_visibility = True if value else False

        @property
        def write_uv_sets(self):
            return self._arg_without_value(self._wuvs, self._write_uv_sets)

        @write_uv_sets.setter
        def write_uv_sets(self, value):
            self._write_uv_sets = True if value else False

    def __init__(self, pre_rool_start_frame=None, dont_skip_unwritten_frames=None):
        self._job = self.Job()
        self._pre_rool_start_frame = pre_rool_start_frame
        self._dont_skip_unwritten_frames = dont_skip_unwritten_frames
        self._verbose = None

        self.cmd = lambda: " ".join(
            [
                "AbcExport ",
                self.pre_rool_start_frame,
                self.dont_skip_unwritten_frames,
                self.verbose,
                self._job.cmd(),
            ]
        )

    @property
    def job(self):
        return '{} "{}"'.format(self._j, self._job.cmd)

    @property
    def pre_rool_start_frame(self):
        """
        The frame to start scene evaluation at.  This is used to set the
        starting frame for time dependent translations and can be used to evaluate
        run-up that isn't actually translated.

        :getter: Return the pre rool start frame
        :setter: Sets the pre rool start frame. This value must be an integer or a float value
        """

        return (
            "{} {}".format(self._prs, self._pre_rool_start_frame)
            if self._pre_rool_start_frame
            else ""
        )

    @pre_rool_start_frame.setter
    def pre_rool_start_frame(self, value):
        if isinstance(value, float) or isinstance(value, int):
            self._pre_rool_start_frame = float(value)
        else:
            raise TypeError("The value must be an integer or a float type.")

    @property
    def dont_skip_unwritten_frames(self):
        """
        When evaluating multiple translate jobs, the presence of this flag decides
        whether to evaluate frames between jobs when there is a gap in their frame
        ranges.
        """

        return "{} ".format(self._duf) if self._dont_skip_unwritten_frames else ""

    @dont_skip_unwritten_frames.setter
    def dont_skip_unwritten_frames(self, value):
        self._dont_skip_unwritten_frames = 1 if value else 0

    @property
    def verbose(self):
        """
        Prints the current frame that is being evaluated.

        """
        return "{} ".format(self._v) if self._verbose else ""

    @verbose.setter
    def verbose(self, value):
        self._verbose = 1 if value else 0
