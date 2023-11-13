"""
This module contains a FastAPI application that generates QR codes from a given secret.
The QR code is returned as a base64 encoded PNG image.
"""
import io
import base64
from fastapi import FastAPI, HTTPException, status
import qrcode


app = FastAPI()

@app.get("/generate_qrcode_base64/{secret}")
async def generate_qrcode_base64(secret: str):
    """
        Qrcode generation
    """

    if not secret:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(secret)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convertir l'image du QR code en base64
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    qr_code_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return {"qrcode_base64": qr_code_base64}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
