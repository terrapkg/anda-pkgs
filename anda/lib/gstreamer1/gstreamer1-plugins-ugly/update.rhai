let html = get("https://gstreamer.freedesktop.org/src/gst-plugins-ugly/?C=M;O=D");
print(find(`gst-plugins-ugly-([\d.]+)\.tar\.xz`, html, 1));
