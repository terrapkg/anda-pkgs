project pkg {
        rpm {
		spec = "mesa.spec"
	}
    labels {
        # multilib = 1
        extra = 1
    }
    arches = ["x86_64", "i386", "aarch64"]
}
