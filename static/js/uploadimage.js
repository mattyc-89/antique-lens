// Get elements
const dropZone = document.querySelector('label[for="img-upload"]');
const fileInput = document.getElementById('img-upload');

// Constants
const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB
const VALID_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];

/* -------------------------------------------------------------------------- */
/* Event Listeners                              */
/* -------------------------------------------------------------------------- */

// 1. Handle the standard file selection (User clicks the button)
fileInput.addEventListener('change', (e) => {
    // We only need to VALIDATE here. The file is already in the input.
    const file = e.target.files[0];
    if (file) {
        if (!validateFile(file)) {
            // If invalid, clear the input so they can try again
            fileInput.value = ''; 
        } else {
             // Success! Proceed to preview or upload
            handleSuccess(file);
        }
    }
});

// 2. Handle the Drop event
dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    toggleHighlight(false); // Remove purple border

    const file = e.dataTransfer.files[0];

    // For drops, we must Validate AND Manually Update the input
    if (file && validateFile(file)) {
        
        // Create a DataTransfer to update the fileInput
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        fileInput.files = dataTransfer.files;

        handleSuccess(file);
    }
});

// 3. UI Feedback Events (Drag Over/Leave)
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    toggleHighlight(true);
});

dropZone.addEventListener('dragleave', () => {
    toggleHighlight(false);
});

/* -------------------------------------------------------------------------- */
/* Helper Functions                               */
/* -------------------------------------------------------------------------- */

/**
 * Checks file type and size.
 * Returns true if valid, false otherwise.
 */
function validateFile(file) {
    // Check Type
    if (!VALID_IMAGE_TYPES.includes(file.type)) {
        alert('Please upload a valid image file (JPEG, PNG, GIF, WEBP).');
        return false;
    }
    
    // Check Size
    if (file.size > MAX_FILE_SIZE) {
        alert('Image size exceeds the 10MB limit.');
        return false;
    }

    return true;
}

/**
 * Toggles the Tailwind classes for the drag zone
 */
function toggleHighlight(active) {
    if (active) {
        dropZone.classList.add('border-purple-600', 'bg-purple-600');
    } else {
        dropZone.classList.remove('border-purple-600', 'bg-purple-600');
    }
}

/**
 * What happens when we have a valid file?
 */
function handleSuccess(file) {
    const previewImage = document.getElementById('img-preview');
    const reader = new FileReader();

    // 1. Tell the reader WHAT to do once it finishes reading the file
    reader.onload = function(e) {
        // e.target.result is the "Data URL" (a long string representing the image)
        previewImage.src = e.target.result;
    }

    // 3. Start reading the file
    reader.readAsDataURL(file);
}