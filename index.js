$(document).ready(() => {
    $('#hamburger-menu').click(() => {
        $('#hamburger-menu').toggleClass('active');
        $('#nav-menu').toggleClass('active');
    })
})

//setting owl carousel

let navText = ["<i class='bx bx-chevron-left'></i>",
                "<i class='bx bx-chevron-right'></i>"];

$('#hero-carousel').owlCarousel({
    items:1,
    dots:true,
    loop:true,
    nav:true,
    navText:navText,
    autoplay:true,
    autoplayHoverPause:true
})

$('#top-movies-slide').owlCarousel({
    items:2,
    dots:false,
    loop:true,
    autoplay:true,
    autoplayHoverPause:true,
    responsive:{
        500:{
            items:3
        },
        1280:{
            items:4
        },
        1600:{
            items:6
        }
    }
})

$('.movies-slide').owlCarousel({
    items: 2,
    dots: false,
    nav: true,
    navText: navText,
    margin: 15,
    responsive:{
        500:{
            items: 3
        },
        1280:{
            items: 4
        },
        1600:{
            items: 6
        }
    }
})

const body = document.body;
const bodyHTML = document.body.innerHTML;
const searchIcon = document.getElementsByClassName('nav-searchicon')[0];
const navBar = document.getElementsByClassName('nav-wrapper')[0];
const movies = document.querySelectorAll('a.movie-item');
const search_input = document.getElementById('nav-searchbar')



searchIcon.addEventListener("click", function(){
    let input_name = search_input.value;
    input_name = input_name.toLowerCase();
    body.innerHTML = "";
    body.append(navBar);
    console.log(input_name);

    body.innerHTML += `
        <div class="hero-section">
            <div class="section">
                <div class="container">
                    <div class="section-header">
                        Search Results
                    </div>
                    <div class="movies-slide carousel-nav-center owl-carousel result-items">
                    </div>
                </div>
            </div>
        </div>
    `;

    const results = document.querySelector(".result-items");
    movies.forEach((e)=>{
        let m_name = e.childNodes[3].childNodes[1].textContent.trim();
        m_name = m_name.toLowerCase();
        if(m_name.includes(input_name))
            results.appendChild(e);
    })

    $('.movies-slide').owlCarousel({
        items: 2,
        dots: false,
        nav: true,
        navText: navText,
        margin: 15,
        responsive:{
            500:{
                items: 3
            },
            1280:{
                items: 4
            },
            1600:{
                items: 6
            }
        }
    })
})