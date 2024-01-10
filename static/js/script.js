const fileInput = document.querySelector('input[type="file"]');
const label = document.querySelector('label[for="file"]');
const h3 = document.querySelector("h3")
const size = document.querySelector("#image-size")
const dimentions = document.querySelector("#image-dimentions")
const form = document.querySelector("form")
let s, d
fileInput.addEventListener("change", function () {
    if (fileInput.files.length > 0) {
        let file = fileInput.files[0];
        const fileName = fileInput.value.split('\\').pop(); // Get the file name from the full path
        const reader = new FileReader();
        reader.onload = function (e) {
            const img = new Image();
            img.src = e.target.result
            img.onload = function () {
                if (file.size > 200 * 1048.576) {
                    h3.innerHTML = "You can only upload images less than 200 KB"
                    size.innerHTML = ""
                    dimentions.innerHTML = ""
                    label.textContent = "No file chosen"
                    dimentions.innerHTML = ""
                    size.innerHTML = ""
                    fileInput.value = ""
                    console.log(fileInput.files)
                }
                else {
                    label.innerHTML = fileName.substring(0, 18)
                    h3.innerHTML = ""
                    s = `size: ${(file.size / 1048.576).toFixed(2)} KB`;
                    d = `dimentions: ${this.width} x ${this.height}`;
                }
            };
        };
        reader.readAsDataURL(file)

    } else {
        h3.innerHTML = ""
        label.textContent = 'No file chosen';
    }
})

form.addEventListener("submit", function (e) {
    const myData = { s, d };
    fetch('/my-django-view-url/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: myData }),
    })
        .then(response => {
        })
        .catch(error => {
        });
})