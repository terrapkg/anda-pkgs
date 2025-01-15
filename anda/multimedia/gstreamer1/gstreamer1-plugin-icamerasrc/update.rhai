rpm.global("commit", gh_commit("intel/icamerasrc"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
}
