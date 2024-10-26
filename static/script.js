document.querySelectorAll('input[name="animal"]').forEach(radio => {
    radio.addEventListener('change', async function() {
        const animalImage = document.getElementById('animalImage');
        const animal = this.value;
        try {
            const response = await fetch(`/image/${animal}`);
            if (response.ok) {
                const blob = await response.blob();
                const imageUrl = URL.createObjectURL(blob);
                animalImage.innerHTML = `<img src="${imageUrl}" alt="${animal}">`;
            } else {
                animalImage.innerHTML = `<p>Error loading ${animal} image</p>`;
            }
        } catch (error) {
            console.error('Error:', error);
            animalImage.innerHTML = `<p>Error loading ${animal} image</p>`;
        }
    });
});

async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select a file');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        document.getElementById('fileInfo').innerHTML = `
            <p>File Name: ${result.filename}</p>
            <p>File Size: ${result.size} bytes</p>
            <p>File Type: ${result.content_type}</p>
        `;
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while uploading the file');
    }
}
