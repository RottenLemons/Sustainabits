<script setup lang="ts">
  import InputText from 'primevue/inputtext';
  import Button from 'primevue/button';
  import DataTable from 'primevue/datatable';
  import { onBeforeMount, ref } from "vue";
  import Textarea from 'primevue/textarea';
  import { awards, createC, friends } from "@/service/TalkToDB";
  import { useToast } from "primevue/usetoast";
  import Toast from 'primevue/toast';
  import { useCookies } from '@vueuse/integrations/useCookies'
  import { useRouter } from 'vue-router';
  import RadioButton from 'primevue/radiobutton';
  import Column from 'primevue/column';
  import Calendar from 'primevue/calendar';

  const toast = useToast(); 
  const cookies = useCookies()
  const dates = ref();
  const privates = ref('false');
  const name = ref(null);
  const description = ref(null);
  const selectedFriend = ref([])
  const items = ref([])
  const selectedAward = ref<any>()
  const items2 = ref([])
  const user = cookies.get('user');
  let router = useRouter();
  if (!user) {
    router.push('/login');
  }

  onBeforeMount(async () => {
      let response = await friends(user.userID);
      items.value = response.friends;
      let response2 = await awards();
      items2.value = response2.awards;
  });

  const submit = async () => {
    if (name.value === null || description.value === null || selectedAward.value.length === 0 || (privates.value === 'true' && selectedFriend.value.length === 0) || dates.value.length !== 2) {
      toast.add({ severity: 'error', summary: 'Error', detail: 'Please fill all fields', life: 3000 });
      return;
    } else {
      let response = await createC(user.userID, name.value, description.value, (privates.value === 'true'), selectedAward.value, selectedFriend.value, dates.value.map((date: any) => new Date(date).toISOString().split('T')[0]));
      router.push('/comps/' + response.comp);
    }
  };



  // Mayybe have a checklist to choose which friends for private?
</script>

<template>

  <main style="width: 100%;">
    <Toast />
    <div class="flex flex-column justify-content-center" style="width: 100%; min-height:94vh;backgroundColor: #337357;">
      <div class="flex flex-column align-items-center gap-5" style="width: 100%;">

        <p style="font-size: 4em; font-weight: bold; color: white; margin-top:2rem; margin-bottom:0rem;">
          Creating Competition
        </p>

        <span class="p-float-label" style="width: 60%; ">
          <InputText size="large" placeholder="Name" inputId="name" style="width: 100%;" v-model="name"/>
          <label for="name">Name</label>
        </span>
        
        <span class="p-float-label" style="width: 60%;">
          <Textarea size="large" placeholder="Description" inputId="description" style="width: 100%;" v-model="description"/>
          <label for="description">Description</label>
        </span>

        <DataTable paginator :rows="5"  v-model:selection="selectedAward" :value="items2" dataKey="awardID" style="width: 60%;">
            <Column selectionMode="single" headerStyle="width: 3rem"></Column>
            <Column field="name" header="Name"  ></Column>
            <Column field="description" header="Description"  ></Column>
        </DataTable>

        <div class="flex justify-content-center align-items-center">
          <p style="font-size: 2em; font-weight: bold; color: white; margin-right: 1rem;">Dates:</p>
          <Calendar v-model="dates" selectionMode="range" :manualInput="false" />
        </div>

        <div class="flex flex-wrap gap-3">
            <div class="flex align-items-center">
                <RadioButton v-model="privates" inputId="true" value="true" :disabled="items.length == 0"/>
                <label for="true" class="ml-2" style="color: white">Private</label>
            </div>
            <div class="flex align-items-center">
                <RadioButton v-model="privates" inputId="false" value="false" />
                <label for="false" class="ml-2" style="color: white">Public</label>
            </div>
        </div>

        
        <DataTable v-if="privates == 'true'" paginator :rows="5"  v-model:selection="selectedFriend" :value="items" dataKey="userID" style="width: 60%;">
            <Column selectionMode="multiple" headerStyle="width: 3rem"></Column>
            <Column field="username" header="Name"  ></Column>
        </DataTable>

        <Button @click="submit" size="large" style="width: 60%; margin-bottom: 2rem;" class="justify-content-center">Submit</Button>
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

