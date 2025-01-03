project "pkg" {
    rpm {
        spec = "nvidia-kmod-common.spec"
    }
    arches = ["x86_64"]
}