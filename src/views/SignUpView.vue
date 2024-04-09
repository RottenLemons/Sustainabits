<script setup lang="ts">
  import InputText from 'primevue/inputtext';
  import Password from 'primevue/password';
  import Divider from 'primevue/divider';
  import Button from 'primevue/button';
  import { ref } from "vue";
  import { signup, UserResponse } from "@/service/TalkToDB";
  import { useToast } from "primevue/usetoast";
  import Toast from 'primevue/toast';
  import { useCookies } from '@vueuse/integrations/useCookies'
  import { useRouter } from 'vue-router';

  const toast = useToast(); 
  const cookies = useCookies()
  const router = useRouter()
  const passwd = ref(null);
  const cpasswd = ref(null);
  const username = ref(null);
  const email = ref(null);

  const submit = async () => {
    if (passwd.value !== cpasswd.value) {
      toast.add({ severity: 'error', summary: 'Error', detail: 'Passwords do not match', life: 3000 });
      return;
    }
    if (username.value === null || email.value === null || passwd.value === null) {
      toast.add({ severity: 'error', summary: 'Error', detail: 'Please fill all fields', life: 3000 });
      return;
    } else {
      let response: UserResponse = await signup(username.value, email.value, passwd.value)
      if (response.result) {
        cookies.set('user', response.user);
        router.push('/');
        toast.add({ severity: 'success', summary: 'Success!', detail: 'Signed In', life: 3000 });
      } else {
        toast.add({ severity: 'error', summary: 'Error', detail: response.message, life: 3000 });
      }
    }
  };
</script>

<template>

  <main style="width: 100%;">
    <Toast />
    <div class="flex flex-column justify-content-center" style="width: 100%; min-height:94vh;background-color: #337357;">
      <div class="flex flex-column align-items-center gap-5" style="width: 100%;">

        <p style="font-size: 4em; font-weight: bold; color: white; margin-top:0;">
          Sign Up
        </p>

        <span class="p-float-label" style="width: 60%;">
          <InputText size="large" placeholder="Username" inputId="username" style="width: 100%;" v-model="username"/>
          <label for="username">Username</label>
        </span>
        
        <span class="p-float-label" style="width: 60%;">
          <InputText size="large" placeholder="Email" inputId="email" style="width: 100%;" v-model="email"/>
          <label for="email">Email</label>
        </span>

        <span class="p-float-label" style="width: 60%;">
          <Password style="width: 100%;" inputClass="w-full text-xl" :inputStyle="{ paddingTop: '0.925rem', paddingBottom: '0.925rem' }" placeholder="Password" v-model="passwd" inputId="password" toggleMask>
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

        <span class="p-float-label" style="width: 60%;">
          <Password style="width: 100%;" inputClass="w-full text-xl" :inputStyle="{ paddingTop: '0.925rem', paddingBottom: '0.925rem' }" placeholder="Confirm Password" v-model="cpasswd" inputId="cpassword" toggleMask>
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
          <label for="password">Confirm Password</label>
        </span>

        <Button @click="submit" size="large" style="width: 60%;" class="justify-content-center">Submit</Button>
        <p style="color: white; margin-top:0;">
          Have an account? <RouterLink style="color: #dad7cd;" to="/login">Login</RouterLink>
        </p>
      </div>
    </div>
  </main>
</template>

