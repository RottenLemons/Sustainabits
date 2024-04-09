<script setup lang="ts">
  import InputText from 'primevue/inputtext';
  import Password from 'primevue/password';
  import Divider from 'primevue/divider';
  import Button from 'primevue/button';
  import { ref } from "vue";
  import { login, UserResponse } from "@/service/TalkToDB";
  import { useToast } from "primevue/usetoast";
  import Toast from 'primevue/toast';
  import { useCookies } from '@vueuse/integrations/useCookies'
  import { useRouter } from 'vue-router';

  const toast = useToast(); 
  const cookies = useCookies()
  const router = useRouter()
  const passwd = ref(null);
  const email = ref(null);

  const submit = async () => {
    if (email.value === null || passwd.value === null) {
      toast.add({ severity: 'error', summary: 'Error', detail: 'Please fill all fields', life: 3000 });
      return;
    } else {
      let response: UserResponse = await login(email.value, passwd.value)
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
    <Toast />
    <main style="width: 100%;">
      <div class="flex flex-column justify-content-center" style="width: 100%; min-height:94vh; background-color: #337357;">
        <div class="flex flex-column align-items-center gap-5" style="width: 100%;">

        <p style="font-size: 4em; font-weight: bold; color: white; margin-top:0;">
          Login
        </p>

        <span class="p-float-label" style="width: 60%;">
          <InputText size="large" placeholder="Email" inputId="email" v-model="email" style="width: 100%;"/>
          <label for="email">Email</label>
        </span>

        <span class="p-float-label" style="width: 60%;">
          <Password style="width: 100%;" inputClass="w-full text-xl" :inputStyle="{ paddingTop: '0.925rem', paddingBottom: '0.925rem' }" placeholder="Password" v-model="passwd" inputId="password" toggleMask>
          </Password>    
          <label for="password">Password</label>
        </span>

        <Button size="large" style="width: 60%;" class="justify-content-center" @click="submit">Submit</Button>
        <p style="color: white; margin-top:0;">
          Dont have an account? <RouterLink style="color: #dad7cd;" to="/signup">Sign Up</RouterLink>
        </p>
      </div>
    </div>
  </main>
</template>
