// Get a reference to the drop zone and the file input
const dropZone = document.querySelector('label[for="gem-img"]');
const fileInput = document.getElementById('gem-img');

// Define valid image MIME types
const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB
const VALID_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];

// Add a change event listener to the file input
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    validateAndProcessFile(file);
});

// Add 'dragover' event listener
dropZone.addEventListener('dragover', (e) => {
    // Prevent default behavior (e.g., opening the file in a new tab)
    e.preventDefault();
    // Add visual feedback to show it's a valid drop zone
    dropZone.classList.add('border-primary', 'bg-blue-600\/5'); // Tailwind classes for highlight
});

// Add 'dragleave' event listener
dropZone.addEventListener('dragleave', () => {
    // Remove visual feedback
    dropZone.classList.remove('border-primary', 'bg-blue-600\/5');
});

// Add 'drop' event listener
dropZone.addEventListener('drop', (e) => {
    // Prevent default browser behavior
    e.preventDefault();
    // Remove visual feedback
    dropZone.classList.remove('border-primary', 'bg-blue-600\/5');

    // Get the file from the drop event
    const file = e.dataTransfer.files[0];
    validateAndProcessFile(file);
});

// Function to validate and process the dropped or selected file
function validateAndProcessFile(file) {
    if (file) {
        if (!VALID_IMAGE_TYPES.includes(file.type)) {
            alert('Please upload a valid image file (JPEG, PNG, GIF, WEBP).');
            return;
            // Clear the file input
            fileInput.value = '';
        }
        if (file.size > MAX_FILE_SIZE) {
            alert('Image size exceeds the 10MB limit. Please upload a smaller file.');
            // Clear the file input
            fileInput.value = '';
            return;
        }

        // Create a new DataTransfer object and add the file to it
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);

        // Assign the file to our hidden input field
        fileInput.files = dataTransfer.files;

        console.log('File is valid and ready to be processed!');
    }
}
