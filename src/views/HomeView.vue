<script setup lang="ts">
  import Image from 'primevue/image';
  import Button from 'primevue/button';
</script>

<template>
  <main style="width: 100%;">
    <div class="flex align-items-center justify-content-center" style="backgroundColor: #344e41; width: 100%; height: 550px;">
      <div class="flex  flex-column align-items-center justify-content-center">
        <p style="font-size: 5em; font-weight: bold; color: white; margin-bottom: 0;" class="font">
          Sustainabits
        </p>
        <p style="font-size: 1.5em; color: white;" class="font">
          Save the planet 1 point at a time
        </p>
        <RouterLink style="text-decoration: none;" to="/signup">
          <Button size="large" style="font-weight: bold; padding-top;: 0.925rem; padding-bottom: 0.925rem; font-size: 2em; color: white">SIGN UP</Button>
        </RouterLink> 
      </div>
      <img alt="logo" src="../assets/logo.svg" width="400" height="400" />
    </div>

    <div class="flex flex-column align-items-center justify-content-center" style="backgroundColor: #a3b18a; width: 100%; height: 700px;">
      <p style="font-size: 3em; font-weight: bold; color: white; margin-bottom: 2em; margin-top: 0em;" class="font">
          Gamify being eco-friendly
      </p>
      <div class="flex align-items-center justify-content-space-around gap-5">
        <div class="flex flex-column align-items-center justify-content-space-around" style="width: 33%;">
          <Image src="https://cdn3d.iconscout.com/3d/premium/thumb/footprint-6855149-5625022.png" width="200" style="margin-top: -2em; margin-bottom: 2em;"/> 
          <p style="font-size: 2em; font-weight: 300; color: white; margin-bottom: 0; margin-top: 0;" class="font text-pretty text-center">
          Track your carbon footprint
          </p>
        </div>

        <div class="flex flex-column align-items-center justify-content-space-around" style="width: 33%">
          <Image src="https://cdn3d.iconscout.com/3d/premium/thumb/badge-3671711-3061912.png" width="200"/> 
          <p style="font-size: 2em; font-weight: 300; color: white; margin-bottom: 0; margin-top: 1em;" class="font text-pretty text-center">
          Earn rewards by complete your goals!
          </p>
        </div>

        <div class="flex flex-column align-items-center justify-content-space-around" style="width: 33%">
          <Image src="https://cdn3d.iconscout.com/3d/premium/thumb/team-battle-7045028-5740242.png" width="200" style="margin-top: -2em; margin-bottom: 2em;"/> 
          <p style="font-size: 2em; font-weight: 300; color: white; margin-bottom: 0; margin-top: 0;" class="font text-pretty text-center">
          Compete with your friends!
          </p>
        </div>
      </div>
    </div>
    
    <div class="flex align-items-center justify-content-center gap-5" style="backgroundColor: #588157; width: 100%; height: 600px;">
      <Image src="https://cdn3d.iconscout.com/3d/premium/thumb/trees-7404343-6043595.png" width="400"/> 
      <div class="flex flex-column align-items-center">
        <p style="font-size: 3em; font-weight: bold; color: white; margin-bottom: 0.75em;" class="font">
          What are you waiting for?
        </p>
        <RouterLink style="text-decoration: none;" to="/signup">
            <Button size="large" style="font-weight: bold; padding-top;: 0.925rem; padding-bottom: 0.925rem; font-size: 2em; color: white">SIGN UP</Button>
        </RouterLink> 
      </div> 
    </div>
  </main>
</template>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@700&display=swap');
  .font {
    font-family: 'Josefin Sans', sans-serif;
  }
</style>