const users = [
    { firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
    { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
    { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
    { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
    { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
    { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
    { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}            
];



const parseUserData = (usersList) => {
    let restructureUserList = []
    for (user of usersList) {
        fullName = `${user.firstName} ${user.lastName}` 
        let userObj = {[fullName] : user.role};
        restructureUserList.push(userObj)
       }
    return restructureUserList
}

console.log(parseUserData(users))

