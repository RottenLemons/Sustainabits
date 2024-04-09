<script setup lang="ts">
  import Avatar from 'primevue/avatar';
  import { useCookies } from '@vueuse/integrations/useCookies';
  import ProgressBar from 'primevue/progressbar';
  import {ref, onBeforeMount} from 'vue';
  import { tree } from "@/service/TalkToDB";
  import Paginator from 'primevue/paginator';

  const cookies = useCookies();
  let user: any = cookies.get('user');
  let items = ref([{}]);
  onBeforeMount(async () => {
      let response = await tree(user.userID);
      items.value = response.trees
      console.log(items.value)
  });
  const first = ref(items.value.length - 1);
</script>

<template>

  <main style="width: 100%;">
    <div class="flex flex-column" style="width: 100%; background-color: #337357;">
      <div class="flex flex-column align-items-center" style="width: 100%;">
        <Paginator v-model:first="first" :rows="1" :totalRecords="items.length" template="PrevPageLink CurrentPageReport NextPageLink" style="margin-top: 2rem;"/>
        <p style="font-size: 4em; font-weight: bold; color: white; margin-top:3rem; margin-bottom: 2rem;">
          {{ items[first].name }}
        </p>

        <Avatar :image="'../../server/images/trees/'+items[first].name+'.jpg'" style="height:20rem; width: 20rem;" shape="circle" />
        
        <p style="font-size: 2em; font-weight: bold; color: white;">
          {{ items[first].description }}
        </p>
        <p v-if="items[first].state == 10" style="font-size: 2em; font-weight: bold; color: white;">
          Completed Date: {{ items[first].completionDate }}
        </p>
      <div v-if="items[first].state != 10" class="flex align-items-center justify-content-center">
        <p style="font-size: 2em; font-weight: bold; color: white; margin-bottom: 2rem; margin-right: 1rem; margin-top: 0rem;">
          Progress: 
        </p>
        <ProgressBar :value="items[first].state/10*100" style="width: 50rem; margin-bottom: 2rem; height: 3rem"></ProgressBar>
      </div>
      <p v-if="items[first].state != 10" style="font-size: 2em; font-weight: bold; color: white; margin-bottom: 2rem; margin-right: 1rem; margin-top: 0rem;">
          Complete more activities to unlock the tree!
        </p>
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