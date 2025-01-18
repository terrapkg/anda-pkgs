project pkg {
    arches = ["i386"]
	rpm {
		spec = "steam.spec"
	}
    // todo: force-arches macro?
    // labels {
    //     multilib = 1
    // }
}
