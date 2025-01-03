project "pkg" {
    rpm {
        spec = "nvidia-driver.spec"
    }
    arches = ["x86_64", "aarch64"]
}