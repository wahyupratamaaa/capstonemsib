<!-- <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" href="../static/EduBooks.png" type="image/png" />

    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap"
      rel="stylesheet"
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
    />
    <title>Profile Section</title>
    <style>
      html {
        scroll-behavior: smooth;
      }
      body {
        background-color: #fff7fc;
        height: 350vh;
        margin: 0;
        font-family: "Poppins", sans-serif;
      }
      * {
        margin: 0;
        padding: 0;
        font-family: "Poppins", sans-serif;
      }
      .container {
        width: 100%;
        height: 35vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #433878;
      }
      .container h1 {
        color: white;
        text-align: center;
        font-size: 2rem;
      }
      .container-text {
        width: auto;
        height: 35vh;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem;
      }

      .box-child {
        width: auto;
        height: auto;
        display: flex;
        flex-wrap: wrap;
        justify-content: end;
        align-items: end;
        padding: 2rem;
        padding-right: 4rem;
        max-width: 40%;
        margin-left: auto;
      }

      .box-child-tengen {
        width: auto;
        height: auto;
        display: flex;
        justify-content: start;
        align-items: start;
        padding: 2rem;
        padding-left: 4rem;
        max-width: 40%;
      }

      .profile-box {
        display: flex;
        align-items: center;
        background-color: white;
        padding: 3rem;
        border-radius: 10px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin: 1rem 0;
        width: 100%;
      }
      .profile-box:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
      }

      .profile-box .profile-picture {
        width: 100px;
        height: 100px;
        background-color: #0056b3;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        margin-right: 1.5rem;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
      }

      .profile-box .profile-picture img {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }

      .profile-details h2 {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
        max-width: 30rem;
        word-wrap: break-word;
        color: gray;
      }

      .profile-details p {
        font-size: 1rem;
        color: gray;
        max-width: 20rem;
        word-wrap: break-word;
        margin-bottom: 0.5rem;
      }

      .icon-profile {
        cursor: pointer;
        width: auto;
        height: auto;
        gap: 2rem;
      }

      .title {
        color: gray;
        margin: 5px 0;
      }
      /* .title p{
            color: red;
        } */

      .garis-vertikal {
        height: 20rem;
        width: 2px;
        border-left: 4px solid gray;
        margin-left: 50px;
        display: flex;
        flex-direction: row;
      }

      .profile-details span {
        font-size: 13px;
        color: gray;
      }
    </style>
    <script>
      let isScrolling = false;
      let scrollDirection = "down";
      let scrollInterval;

      function autoScroll() {
        if (!isScrolling) {
          if (scrollDirection === "down") {
            window.scrollBy(0, 100);
            if (
              window.scrollY + window.innerHeight >=
              document.documentElement.scrollHeight
            ) {
              scrollDirection = "up";
            }
          } else if (scrollDirection === "up") {
            window.scrollBy(0, -100);
            if (window.scrollY <= 0) {
              scrollDirection = "down";
            }
          }
        }
      }

      function startAutoScroll() {
        scrollInterval = setInterval(autoScroll, 30);
      }

      window.addEventListener("wheel", function (event) {
        isScrolling = true;
        clearInterval(scrollInterval);
        setTimeout(function () {
          isScrolling = false;
          startAutoScroll();
        }, 2000);
      });

      window.onload = startAutoScroll;
    </script>
  </head>
  <body>
    <audio autoplay loop>
      <source src="../static/audio/ambis2.mp3" type="audio/mp3" />
      Browser Anda tidak mendukung audio.
    </audio>

    <div class="container mx-auto p-4">
      <h1
        class="text-2xl md:text-3xl font-bold text-center"
        style="color: #f0f0f0"
      >
        Kesan Kesan <br />
        <span
          class="flex justify-center items-center"
          style="display: flex; justify-content: center; align-items: center"
        >
          Developer Dibalik
          <img
            src="../static/developer.png"
            alt="developer"
            style="width: 12%; height: auto; margin-left: 8px"
          />
        </span>
        Capstone MSIB Batch 7 Fullstack Web Developer at LearningX Academy
        <br />
        <span
          class="text-xs"
          style="font-size: 15px; color: #f0f0f0; font-weight: 400"
        >
          Gedung Pacific Century Place Jl. Jenderal Sudirman KAV 52-53 RT. 005
          RW 003 Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 📍
        </span>
      </h1>
    </div>

    <div class="box-child">
      <div class="profile-box">
        <div class="profile-picture">
          <img src="../static/human/atmin.jpeg" alt="Profile Picture" />
        </div>
        <div class="profile-details">
          <h2>Wahyu Pratama S.Kom.</h2>
          <h4 class="title">Role : Developer/UIUX at EduBooks</h4>
          <p>
            Terima kasih sebesar-besarnya kepada <strong>Kak Himawa</strong> dan
            seluruh mentor di LearningX Academy atas satu semester yang sangat
            berharga sebagai mentor dalam pelatihan Fullstack Web Developer 😹
          </p>
          <span>Malang, Indonesia</span>
          <div class="icon-profile">
            <a href="https://www.linkedin.com/in/wahyupratama24/"
              ><i class="fa-brands fa-linkedin"></i
            ></a>
            <i class="fa-brands fa-instagram"></i>
            <i class="fa-brands fa-github"></i>
          </div>
        </div>
      </div>
    </div>

    <div class="box-child-tengen">
      <div class="profile-box">
        <div class="profile-picture">
          <img src="../static/icon.webp" alt="Profile Picture" />
        </div>
        <div class="profile-details">
          <h2>Anomali</h2>
          <h4 class="title">Role : Anomali</h4>
          <p>
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Est
            aperiam quo quibusdam quaerat cum necessitatibus cumque iste
            possimus, amet repellat sequi provident tempore, dignissimos animi
            soluta. Earum voluptates delectus accusamus.
          </p>
          <span>Malang, Indonesia</span>
          <div class="icon-profile">
            <i class="fa-brands fa-linkedin"></i>
            <i class="fa-brands fa-instagram"></i>
            <i class="fa-brands fa-github"></i>
          </div>
        </div>
      </div>
    </div>

    <div class="box-child">
      <div class="profile-box">
        <div class="profile-picture">
          <img src="../static/icon.webp" alt="Profile Picture" />
        </div>
        <div class="profile-details">
          <h2>Anomali</h2>
          <h4 class="title">Anomali</h4>
          <p>
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Est
            aperiam quo quibusdam quaerat cum necessitatibus cumque iste
            possimus, amet repellat sequi provident tempore, dignissimos animi
            soluta. Earum voluptates delectus accusamus.
          </p>
          <span>Malang, Indonesia</span>
          <div class="icon-profile">
            <i class="fa-brands fa-linkedin"></i>
            <i class="fa-brands fa-instagram"></i>
            <i class="fa-brands fa-github"></i>
          </div>
        </div>
      </div>
    </div>

    <div
      class="garis-vertikal"
      style="display: flex; flex-direction: row; align-items: flex-start"
    >
      <div
        class="garis"
        style="width: 2px; background-color: black; height: 100%"
      ></div>
      <div
        style="
          display: flex;
          align-items: center;
          justify-content: center;
          padding-left: 20px;
          width: auto;
          height: auto;
        "
      >
        <span style="width: 500px; color: gray"
          ><strong>EduBooks</strong> hadir untuk mengingatkan pentingnya membaca
          di era digital, sebagai kunci untuk memperluas pengetahuan dan
          memperkaya diri melalui buku, yang tetap relevan di tengah
          perkembangan teknologi.</span
        >
      </div>
    </div>
    <div class="container-text" style="margin-top: 15rem">
      <span
        style="
          padding: 5rem;
          display: flex;
          align-items: center;
          justify-content: center;
          text-align: center;
          width: 70%;
          color: gray;
        "
        >Jangan berfikir tidak mungkin,tapi berfikirlah bagaimana caranya</span
      >
    </div>
  </body>
</html> -->