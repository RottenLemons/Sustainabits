<script setup lang="ts">
  import InputText from 'primevue/inputtext';
  import Password from 'primevue/password';
  import Divider from 'primevue/divider';
  import Button from 'primevue/button';
  import { ref } from "vue";

  const value = ref(null);
</script>

<template>
  <main style="width: 100%;">
    <div class="flex flex-column justify-content-center" style="width: 100%; height:94vh; background-color: #588157; opacity: 0.8; background-image: radial-gradient(circle at center center, #344e41, #588157), repeating-radial-gradient(circle at center center, #344e41, #344e41, 40px, transparent 80px, transparent 40px); background-blend-mode: multiply;">
      <div class="flex flex-column align-items-center gap-5" style="width: 100%;">

        <p style="font-size: 4em; font-weight: bold; color: white; margin-top:0;">
          Login
        </p>

        <span class="p-float-label" style="width: 60%;">
          <InputText size="large" placeholder="Email" inputId="email" style="width: 100%;"/>
          <label for="email">Email</label>
        </span>

        <span class="p-float-label" style="width: 60%;">
          <Password style="width: 100%;" inputClass="w-full text-xl" :inputStyle="{ paddingTop: '0.925rem', paddingBottom: '0.925rem' }" placeholder="Password" v-model="value" inputId="password" toggleMask>
            <template #footer >
              <Divider />
              <p class="mt-2">Suggestions</p>
              <ul class="pl-2 ml-2 mt-0" style="line-height: 1.5">
                  <li>At least one lowercase</li>
                  <li>At least one uppercase</li>
                  <li>At least one numeric</li>
                  <li>Minimum 8 characters</li>
              </ul>
            </template>
          </Password>    
          <label for="password">Password</label>
        </span>

        <Button size="large" style="width: 60%;" class="justify-content-center">Submit</Button>
        <p style="color: white; margin-top:0;">
          Dont have an account? <RouterLink style="color: #dad7cd;" to="/signup">Sign Up</RouterLink>
        </p>
      </div>
    </div>
  </main>
</template>
