
let projectsUrl = "http://localhost:8000/api/projects/"

let getProjects = () => {
    fetch(projectsUrl)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            buildProjects(data)
        })
}

let buildProjects = () => {
    let projectsWrapper = document.getElementById('project-wrapper')

    for (let i = 0; projects.length > i; i++) {
        let project = projects[i]

        let projectCard = `
            <div class="project--card">
                <img src="http://localhost:8000${project.featured_image}"/>

                <div>
                    <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option">&#43;</storng>
                        <strong class="vote--option">&#722;</storng>
                    </div>
                    <i> ${project.vote_ratio}% Positive feedback </i>
                    <p> ${project.description.substirng(0, 150)} </p>
                </div>
            </div>
        `
        projectsWrapper.innerHTML += projectCard
    }
}

getProjects()
