export const Users = {
    getData() {
        return [
                {
                    "name": "Jamal Horn",
                    "country": "Germany",
                    "email": "facilisis@protonmail.com",
                    "postalZip": "68464"
                },
                {
                    "name": "Jason Clarke",
                    "country": "Germany",
                    "email": "metus@outlook.ca",
                    "postalZip": "O5 4RJ"
                },
                {
                    "name": "Zachary Bond",
                    "country": "South Africa",
                    "email": "ut@yahoo.com",
                    "postalZip": "305262"
                },
                {
                    "name": "Igor Ingram",
                    "country": "South Africa",
                    "email": "ornare.lectus.justo@outlook.ca",
                    "postalZip": "5134-1821"
                },
                {
                    "name": "Ayanna Love",
                    "country": "Sweden",
                    "email": "lorem@icloud.com",
                    "postalZip": "805365"
                },
                {
                    "name": "Samuel Richards",
                    "country": "South Africa",
                    "email": "libero.est@icloud.org",
                    "postalZip": "8896"
                },
                {
                    "name": "Yoshi Stevens",
                    "country": "Colombia",
                    "email": "vitae.dolor@protonmail.edu",
                    "postalZip": "18601-92454"
                },
                {
                    "name": "Kane Barton",
                    "country": "New Zealand",
                    "email": "feugiat.non@google.edu",
                    "postalZip": "65652-141"
                },
                {
                    "name": "Brenden Peterson",
                    "country": "Sweden",
                    "email": "sapien.cursus@icloud.net",
                    "postalZip": "26368"
                },
                {
                    "name": "Jesse Martinez",
                    "country": "Mexico",
                    "email": "ipsum.dolor.sit@aol.edu",
                    "postalZip": "50118"
                }
            ]
    },
    getUsers() {
        return Promise.resolve(this.getData());
    },};