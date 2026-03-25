import http from 'k6/http';

export default function () {
    http.post(
        'http://127.0.0.1:8000/generate',
        JSON.stringify({
            prompt: "Explain gravity"
        }),
        {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer test123'
            }
        }
    );
}