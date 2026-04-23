document.addEventListener("DOMContentLoaded", function () {
    const input = document.querySelector('input[type="file"]');
    if (!input) return;

    input.addEventListener("change", function () {
        const file = this.files[0];
        if (!file) return;

        if (!file.type.startsWith("image/")) {
            alert("الملف يجب أن يكون صورة فقط!");
            this.value = "";
            return;
        }

        if (file.size > 3 * 1024 * 1024) {
            alert("الصورة أكبر من 3MB!");
            this.value = "";
            return;
        }

        const reader = new FileReader();
        reader.onload = function (e) {
            let preview = document.getElementById("preview-image");
            if (!preview) {
                preview = document.createElement("img");
                preview.id = "preview-image";
                preview.style.width = "150px";
                preview.style.marginTop = "10px";
                preview.style.borderRadius = "10px";
                preview.style.objectFit = "cover";
                input.parentNode.appendChild(preview);
            }
            preview.src = e.target.result;
        };
        reader.readAsDataURL(file);
    });
});