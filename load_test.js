import http from 'k6/http';
import { sleep } from 'k6';

const users = ["user1", "user2", "user3", "user4", "user5"];

export default function () {
    const user = users[Math.floor(Math.random() * users.length)];

    const prompts = [
        "Explain gravity",
        "What is AI?",
        "Tell me a joke",
        "Explain black holes"
    ];

    const prompt = prompts[Math.floor(Math.random() * prompts.length)];

    http.post(
        'http://127.0.0.1:8000/generate',
        JSON.stringify({ prompt }),
        {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${user}`
            }
        }
    );

    sleep(1);
}