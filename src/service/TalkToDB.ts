import axios from "axios";

export class UserResponse {
    result!: boolean;
    user!: any;
    message!: string;
    achievements!: any[];
} 

export class CO2Response {
    editable!: boolean;
    items!: any;
    limit!: number;
    used!: number;
} 

export async function friends(userID: string) {
    let response = await axios.post("http://localhost:8080/friends", {
        userID: userID
    });
    return response.data;  
}

export async function getUser(userID: string) {
    let response = await axios.post("http://localhost:8080/userU", {
        userID: userID
    });
    return response.data;  
}

export async function friendChange(userID: string, friendID: string, add: boolean) {
    let response = await axios.post("http://localhost:8080/friendChange", {
        userID: userID,
        friendID: friendID,
        add: add
    });
    return response.data;  
}

export async function joinC(userID: string, competitionID: string) {
    let response = await axios.post("http://localhost:8080/joinC", {
        userID: userID,
        competitionID: competitionID
    });
    return response.data;  
}

export async function tree(userID: string) {
    let response = await axios.post("http://localhost:8080/trees", {
        userID: userID
    });
    return response.data;  
}

export async function insertAct(userID: string, activityID: string) {
    let response = await axios.post("http://localhost:8080/insertAct", {
        userID: userID,
        activityID: activityID
    });
    return response.data;  
}

export async function insertEvent(userID: string, eventID: string) {
    let response = await axios.post("http://localhost:8080/insertEvent", {
        userID: userID,
        eventID: eventID
    });
    return response.data;  
}

export async function updateU(userID: string, username: string,  email: string,image: string, limit: number) {
    let response = await axios.post("http://localhost:8080/updateU", {
        userID: userID,
        username: username,
        email: email,
        image: image,
        limit: limit
    });
    return response.data;  
}

export async function createC(userID: string, name: string, description: string, privates: boolean, award: any, friends: any[], dates: any[]) {
    let response = await axios.post("http://localhost:8080/createComp", {
        userID: userID,
        name: name,
        description: description,
        private: privates,
        award: award,
        friends: friends,
        dates: dates
    });
    return response.data;  
}

export async function awards() {
    let response = await axios.get("http://localhost:8080/awards");
    return response.data;  
}

export async function competitions(userID: string) {
    let response = await axios.post("http://localhost:8080/competitions", {
        userID: userID
    });
    return response.data;  
}

export async function searchC(userID: string, query: string) {
    let response = await axios.post("http://localhost:8080/searchC", {
        userID: userID,
        query: query
    });
    return response.data;  
}

export async function searchE(userID: string, query: string) {
    let response = await axios.post("http://localhost:8080/searchE", {
        userID: userID,
        query: query
    });
    return response.data;  
}

export async function searchF(userID: string, query: string) {
    let response = await axios.post("http://localhost:8080/searchF", {
        userID: userID,
        query: query
    });
    return response.data;  
}


export async function competition(userID: string, competitionID: string | string) {
    let response = await axios.post("http://localhost:8080/competition", {
        userID: userID,
        competitionID: competitionID
    });
    return response.data;  
}

export async function activities(treeID: string, userID: string, date: string, start: string) {
    let response = await axios.post("http://localhost:8080/activities", {
        treeID: treeID,
        userID: userID,
        date: date,
        start: start
    });
    return response.data;  
}

export async function searchA(treeID: string, userID: string, date: string, start: string, query: string) {
    let response = await axios.post("http://localhost:8080/searchA", {
        treeID: treeID,
        userID: userID,
        date: date,
        start: start,
        query: query
    });
    return response.data;  
}

export async function events(userID: string) {
    let response = await axios.post("http://localhost:8080/events", {
        userID: userID
    });
    return response.data;  
}

export async function users(userID: string) {
    let response = await axios.post("http://localhost:8080/users", {
        userID: userID
    });
    return response.data;  
}

export async function co2(userID: string, date: string) {
    let response = await axios.post("http://localhost:8080/co2", {
        userID: userID,
        date: date
    });
    return response.data;  
}

export async function co2Change(userID: string, date: string, categoryID: number, dol: number, remove: boolean) {
    let response = await axios.post("http://localhost:8080/co2Change", {
        userID: userID,
        date: date,
        categoryID: categoryID,
        dol: dol,
        remove: remove
    });

    return response.data;  
}


export async function login(email: string, password: string) {
    let response = await axios.post("http://localhost:8080/login", {
        email: email,
        password: password
    });

    return response.data;  
}

export async function signup(username:string, email: string, password: string) {
    let response = await axios.post("http://localhost:8080/signup", {
        username: username,
        email: email,
        password: password
    });
    
    return response.data;
}