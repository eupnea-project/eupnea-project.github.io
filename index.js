const chevronTriggerY = 100;

function initChevron() {
    const chevron = document.querySelector('.chevron');
    chevron.onclick = () => {
        window.scrollTo({
            behavior: "smooth",
            top: window.innerHeight,
        });
    };

    window.onscroll = (_) => {
        chevron.classList.toggle("hidden", window.scrollY >= chevronTriggerY);
    };
}

initChevron();