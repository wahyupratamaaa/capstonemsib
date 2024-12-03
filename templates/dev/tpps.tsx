<!DOCTYPE html>
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
      .box-child,
      .box-child-tengen {
        width: auto;
        height: auto;
        display: flex;
        flex-wrap: wrap;
        justify-content: end;
        align-items: end;
        padding: 2rem;
        padding-right: 4rem;
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
    <script type="module">
      const renderProfiles = async () => {
        const boxChild = document.querySelector(".box-child");
        const boxChildTengen = document.querySelector(".box-child-tengen");

        try {
          // Ambil data dari JSON
          const response = await fetch("../../static/data.json");
          const profiles = await response.json();

          profiles.forEach((profile, index) => {
            const profileHTML = `
              <div class="profile-box">
                <div class="profile-picture">
                  <img src="${profile.img}" alt="${profile.name}" />
                </div>
                <div class="profile-details">
                  <h2>${profile.name}</h2>
                  <h4 class="title">Role: ${profile.role}</h4>
                  <p>${profile.description}</p>
                  <span>${profile.location}</span>
                  <div class="icon-profile">
                    <a href="${profile.socials.linkedin}" target="_blank">
                      <i class="fa-brands fa-linkedin"></i>
                    </a>
                    <a href="${profile.socials.instagram}" target="_blank">
                      <i class="fa-brands fa-instagram"></i>
                    </a>
                    <a href="${profile.socials.github}" target="_blank">
                      <i class="fa-brands fa-github"></i>
                    </a>
                  </div>
                </div>
              </div>
            `;
            // Render ke container sesuai index
            if (index % 2 === 0) {
              boxChild.innerHTML += profileHTML;
            } else {
              boxChildTengen.innerHTML += profileHTML;
            }
          });
        } catch (error) {
          console.error("Error fetching profiles:", error);
        }
      };

      renderProfiles();
    </script>
  </head>
  <body>
    <div class="container mx-auto p-4">
      <h1>Kesan</h1>
    </div>
    <div class="box-child"></div>
    <div class="box-child-tengen"></div>
  </body>
</html>
