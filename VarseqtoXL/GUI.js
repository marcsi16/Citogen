document.addEventListener('DOMContentLoaded', function () {
    const sourceFileInput = document.getElementById('sourceFile');
    const destinationFileInput = document.getElementById('destinationFile');
    const browseSourceButton = document.getElementById('browseSource');
    const browseDestinationButton = document.getElementById('browseDestination');
    const startButton = document.getElementById('startButton');

    // Function to trigger a click event on an input element
    function openFileBrowser(inputElement) {
        const evt = new MouseEvent('click', {
            bubbles: false,
            cancelable: true,
            view: window,
        });
        inputElement.dispatchEvent(evt);
    }

    // Open a file dialog for selecting the source Excel file
    browseSourceButton.addEventListener('click', () => {
        openFileBrowser(sourceFileInput);
    });

    // Display selected file's path
    sourceFileInput.addEventListener("change", function () {
        const selectedSourceFile = sourceFileInput.files[0];

        if (selectedSourceFile) {
            const filePath = selectedSourceFile.name;
            selectedSourceFilePath.textContent = `Selected File: ${filePath}`;
        } else {
            selectedSourceFilePath.textContent = "No file selected.";
        }
    });

    // Open a file dialog for selecting the destination Excel file
    browseDestinationButton.addEventListener('click', () => {
        openFileBrowser(destinationFileInput);
    });

    // Display selected file's path
    destinationFileInput.addEventListener("change", function () {
        const selectedDestFile = destinationFileInput.files[0];

        if (selectedDestFilePath) {
            const filePath = selectedDestFile.name;
            selectedDestFilePath.textContent = `Selected File: ${filePath}`;
        } else {
            selectedDestFilePath.textContent = "No file selected.";
        }
    });

    // Start button click handler
    startButton.addEventListener('click', () => {
        const sourceFile = sourceFileInput.value;
        const destinationFile = destinationFileInput.value;

        if (sourceFile && destinationFile) {
            const { spawn } = require('child_process');
            const pythonProcess = spawn('python', ['VarseqtoXL.py', sourceFile, destinationFile]);

            // Handle Python script's output (optional)
            pythonProcess.stdout.on('data', (data) => {
                console.log(`Python stdout: ${data}`);
            });

            pythonProcess.stderr.on('data', (data) => {
                console.error(`Python stderr: ${data}`);
            });

            pythonProcess.on('close', (code) => {
                console.log(`Python script exited with code ${code}`);
            });

            alert(`Processing source file: ${sourceFile}\nSaving to destination file: ${destinationFile}`);
        } else {
            alert('Both source and destination files are required.');
        }
    });
})