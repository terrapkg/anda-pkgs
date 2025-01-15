let html = get("https://gstreamer.freedesktop.org/src/gst-plugins-bad/?C=M;O=D");
print(find(`gst-plugins-bad-([\d.]+)\.tar\.xz`, html, 1));
