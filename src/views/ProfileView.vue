<script setup lang="ts">
  import Avatar from 'primevue/avatar';
  import { useCookies } from '@vueuse/integrations/useCookies';
  import DataTable from 'primevue/datatable';
  import {ref, onBeforeMount} from 'vue';
  import { getUser, updateU } from "@/service/TalkToDB";
  import Button from 'primevue/button';
  import InputText from 'primevue/inputtext';
  import FileUpload from 'primevue/fileupload';
  import Column from 'primevue/column';
  import { useRouter } from 'vue-router';

  const cookies = useCookies();
  let user: any = cookies.get('user');
  let router = useRouter();
  if (!user) {
    router.push('/login');
  }
  let items = ref([{}]);
  const edit = ref(false);
  const username = ref(user.username);
  const email = ref(user.email);
  const limit = ref(user.co2Limit);
  const base64data = ref<any>(null);

  onBeforeMount(async () => {
      let response = await getUser(user.userID);
      items.value = response.achievements
      cookies.set('user', response.user);
      user = response.user;
  });
  
  const edits = () => {
    edit.value = true;
  }
  const reset = () => {
    edit.value = false;
    username.value = user.username;
    email.value = user.email;
    limit.value = user.co2Limit;
    base64data.value = null;
  }

  const save = async () => {
    let response = await updateU(user.userID, username.value, email.value, base64data.value, limit.value);
    cookies.set('user', response.user);
    user = response.user;
    edit.value = false;
    reset();
  }

  
const customBase64Uploader = async (event: any) => {
    const file = event.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onloadend = function () {
        base64data.value = reader.result;
    };
};

</script>

<template>

  <main style="width: 100%;">
    <div class="flex flex-column" style="width: 100%; background-color: #337357;">
      <div class="flex flex-column align-items-center" style="width: 100%;">
        <div class="flex flex-row justify-content-center align-items-center gap-3">
          <p v-if="!edit" style="font-size: 4em; font-weight: bold; color: white; margin-top:5rem; margin-bottom: 3rem;">
            {{ user.username }}
          </p>
          <InputText v-if="edit" type="text" v-model="username" style="margin-top:5rem; margin-bottom: 3rem; font-size: 4em; padding-top: 1rem; padding-bottom: 1rem; width: 50%"/>
          <Button v-if="!edit" @click="edits" icon="pi pi-pencil" style="color: white; margin-top:5rem; margin-bottom: 3rem; font-size: 4em;" text rounded />
          <Button v-if="edit" @click="save" icon="pi pi-check" style="color: white; margin-top:5rem; margin-bottom: 3rem; font-size: 4em;" text rounded />
          <Button v-if="edit" @click="reset" icon="pi pi-times" style="color: white; margin-top:5rem; margin-bottom: 3rem; font-size: 4em;" text rounded />

        </div>
        <Avatar v-if="!edit" :image="'../../server/images/'+user.userimage" style="height:20rem; width: 20rem;" shape="circle" />
        <FileUpload v-if="edit" :multiple="false" accept="image/*" :maxFileSize="1000000" customUpload @uploader="customBase64Uploader">
          <template #empty>
                <p>Drag and drop files to here to upload.</p>
            </template>
        </FileUpload>
        <div class="flex justify-content-center align-items-center gap-2" style="margin-top: 3rem;">
          <p style="font-size: 2em; font-weight: bold; color: white;">
          Email:
        </p>

        <p v-if="!edit" style="font-size: 2em; font-weight: bold; color: white;">
         {{ user.email }}
        </p>

        <InputText v-if="edit" type="text" v-model="email" style="font-size: 2em; padding-top: 0.5rem; padding-bottom: 0.5rem; width: 80%"/>
      </div>
        <p style="font-size: 2em; font-weight: bold; color: white;">
          Total Points: {{ user.totalPoints }}
        </p>

        <div class="flex justify-content-center align-items-center gap-2">
          <p style="font-size: 2em; font-weight: bold; color: white;">
            CO2 Usage Limit:
        </p>

        <p v-if="!edit" style="font-size: 2em; font-weight: bold; color: white;">
         {{ user.co2Limit }}
        </p>

        <InputText v-if="edit" type="number" v-model="limit" style="font-size: 2em; padding-top: 0.5rem; padding-bottom: 0.5rem; width: 80%"/>
      </div>

        <DataTable v-if="!items && !edit" showGridlines paginator :rows="5" :value="items" editMode="row" dataKey="id"
            :pt="{
                table: { style: 'min-width: 50rem' }
            }"
        >
            <Column field="name" header="Name" style="width: 70%">
            </Column>
            <Column field="count" header="Count" bodyStyle="text-align:center" style="width: 30%">
            </Column>
        </DataTable>
      </div>
    </div>
  </main>
</template>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@700&display=swap');
  .font {
    font-family: 'Josefin Sans', sans-serif;
  }

  .p-paginator {
    border-radius: 0px;
  }
</style>