<script setup lang="ts">
  import Image from 'primevue/image';
  import Button from 'primevue/button';
  import { useRoute } from 'vue-router'
  const route = useRoute()
  const id = route.params.username;
</script>

<template>
  <main style="width: 100%;">
    <div class="flex align-items-center justify-content-center" style="backgroundColor: #344e41; width: 100%; height: 550px;">
      <div class="flex  flex-column align-items-center justify-content-center">
        <p style="font-size: 5em; font-weight: bold; color: white; margin: 0;" class="font">
          Sustainabits
        </p>
        <p style="font-size: 2em; color: white; margin-top: 1em;" class="font">
          Save the planet 1 bit at a time
        </p>
        <RouterLink v-if="typeof id === 'undefined' || id === ''" style="text-decoration: none;" to="/signup">
          <Button style="font-weight: bold; padding: 2rem; font-size: 2.5em; color: white">SIGN UP</Button>
        </RouterLink> 
        <p v-else style="font-size: 2em; color: white; margin-top: 1em;" class="font">
          Hello {{ id }}
        </p>
      </div>
      <img alt="logo" src="../assets/logo.svg" width="400" height="400" />
    </div>

    <div class="flex flex-column align-items-center justify-content-center" style="backgroundColor: #588157; width: 100%; height: 700px;">
      <p style="font-size: 4em; font-weight: bold; color: white; margin-bottom: 2em; margin-top: 0em;" class="font">
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
    
    <div class="flex align-items-center justify-content-center gap-5" style="backgroundColor: #3a5a40; width: 100%; height: 600px;">
      <Image src="https://cdn3d.iconscout.com/3d/premium/thumb/trees-7404343-6043595.png" width="400"/> 
      <div class="flex flex-column align-items-center">
        <p style="font-size: 4em; font-weight: bold; color: white; margin-bottom: 0.75em; margin-top: 0.5em;" class="font">
          What are you waiting for?
        </p>
        <RouterLink style="text-decoration: none;" to="/signup">
          <Button style="font-weight: bold; padding: 2rem; font-size: 2.5em; color: white">SIGN UP</Button>
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