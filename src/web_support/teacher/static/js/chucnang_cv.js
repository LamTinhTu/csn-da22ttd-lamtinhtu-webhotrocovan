document.getElementById("btnEdit").addEventListener("click", function () {
    let editModal = new bootstrap.Modal(document.getElementById("addAdvisorModal"));
    document.getElementById("addAdvisorModalLabel").innerText = "Sửa Thông Tin";
    editModal.show();
});
// Form thêm
document.getElementById("btnAdd").addEventListener("click", function () {
    let addModal = new bootstrap.Modal(document.getElementById("addAdvisorModal"));
    addModal.show();
});
// Form xoá
document.getElementById("btnDelete").addEventListener("click", function () {
    let deleteModal = new bootstrap.Modal(document.getElementById("deleteConfirmationModal"));
    deleteModal.show();
});