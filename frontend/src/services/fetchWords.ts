const GET_WORD_LIST_URL = 'http://localhost:5000/solve'

async function getWords(object: {letters: string[], specialLetter: string}) {
    try {
        const res = await fetch(GET_WORD_LIST_URL, {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(object)
        });

        if (!res.ok) {
            return Error('unable to fetch words')
        }

        return await res.json();

    } catch (error) {
        return Error('unable to fetch words.')
    }
}

export default getWords;