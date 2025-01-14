project "pkg" {
    rpm {
        spec = "libnvidia-container.spec"
    }
    arches = ["x86_64", "aarch64", "i386"]
    labels = {
        subrepo = "nvidia"
        mock = 1
    }
}
