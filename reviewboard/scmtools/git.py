import subprocess
        SCMTool.__init__(self, repository)
        self.client = GitClient(repository.path, repository.raw_file_url)
    def check_repository(cls, path, username=None, password=None):
        client = GitClient(path)
        super(GitTool, cls).check_repository(client.path, username, password)
        # We have no use for recording this info so skip it
        if self._is_newfile_or_deleted_change(linenum):
    def _is_newfile_or_deleted_change(self, linenum):
        line = self.lines[linenum]
        return (line.startswith("new file mode")
                or line.startswith("deleted file mode"))
    def __init__(self, path, raw_file_url=None):
                return urllib2.urlopen(url).read()
                return urllib2.urlopen(url).geturl()
        return subprocess.Popen(
            ['git'] + args,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            close_fds=(os.name != 'nt')
        )
            return 'ssh://%s%s%s' % (m.group('username'),