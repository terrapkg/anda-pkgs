rpm.global("commit", gh_commit("falkTX/Carla"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    rpm.global("ver", gh("falkTX/Carla"));
}
