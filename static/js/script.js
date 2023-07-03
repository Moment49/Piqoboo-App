nav_links = document.querySelectorAll('.nav_link')

for (let i = 0; i < nav_links.length; i++){
    nav_links[i].addEventListener('click', ()=>{
        document.querySelector('.active').classList.remove('active')
        nav_links[i].classList.add('active')
    })
}
