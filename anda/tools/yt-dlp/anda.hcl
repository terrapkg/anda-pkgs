project pkg {
	rpm {
		spec = "yt-dlp-nightly.spec"
	}
	labels {
		nightly = "1"
		mock = 1
	}
}
