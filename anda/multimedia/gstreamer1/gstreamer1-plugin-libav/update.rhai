let html = get("https://gstreamer.freedesktop.org/src/gst-libav/?C=M;O=D");
let v = print(find(`gst-libav-([\d.]+)\.tar\.xz`, html, 1));
rpm.version(v);
