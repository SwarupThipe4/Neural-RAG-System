@echo off
echo Starting RAG Chatbot...
python setup.py
if %errorlevel% equ 0 (
    echo.
    echo Starting Streamlit app...
    streamlit run app.py
) else (
    echo Setup failed. Please check the error messages above.
    pause
)