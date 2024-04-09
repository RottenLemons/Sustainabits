<script setup lang="ts">
  import { useRoute, useRouter } from 'vue-router';
  import { ref, onBeforeMount, watch } from "vue";
  import { useCookies } from '@vueuse/integrations/useCookies';
  import { events, insertEvent, searchE } from "@/service/TalkToDB";
  import DataView from 'primevue/dataview';
  import Button from 'primevue/button';
  import Dropdown from 'primevue/dropdown';
  import InputText from 'primevue/inputtext';

  const cookies = useCookies()
  const route = useRoute()
  const id = route.params.username;
  const user = cookies.get('user');
  let router = useRouter();
  if (!user) {
    router.push('/login');
  }
  let items = ref<{ points: number, numFriendsAttending: number, date: string, name: string }[]>([]);
  let sorts = ref('date');
  
  onBeforeMount(async () => {
      let response = await events(user.userID);
      items.value = response.events
  });

  watch(sorts, (value) => {

    if (sorts.value['name'] === 'Date') {
      items.value.sort((a, b) => {
        return new Date(a.date).getTime() - new Date(b.date).getTime();
      });
    } else if (sorts.value['name'] === 'Points') {

      items.value.sort((a, b) => {
        return b.points - a.points;
      });
    } else if (sorts.value['name'] === 'Friends') {

      items.value.sort((a, b) => {
        return b.numFriendsAttending - a.numFriendsAttending;
      });
    }
  });

  const sortsby = ref([
    { name: 'Date' },
    { name: 'Points'},
    { name: 'Friends'}
]);
  
const save = async (event: any) => {
    let res1 = await insertEvent(user.userID,event.eventID);
    let response = await events(user.userID);
      items.value = response.events
  };

const query = ref('')

watch(query, async (val) => {
  let response = await searchE(user.userID, query.value);
  items.value = response.events
});
</script>

<template>
  <main style="width: 100%;">
    <div class="flex flex-column align-items-center justify-content-center" style="backgroundColor: #337357; width: 100%; min-height: 94vh;">
      <p style="font-size: 4em; font-weight: bold; color: white; margin-bottom: 0.75em; margin-top: 0.5em;" class="font">Events</p>
        <DataView paginator :rows="3" :value="items" dataKey="userID" style="width: 70%;">
          <template #header>
              <div class="flex justify-content-between">
                <Dropdown v-model="sorts" :options="sortsby" optionLabel="name" placeholder="Sort By" class="w-full md:w-14rem"/>
                  <IconField iconPosition="left">
                      <InputIcon>
                          <i class="pi pi-search" />
                      </InputIcon>
                      <InputText style="margin-left: 1rem;" placeholder="Keyword Search" v-model="query"/>
                  </IconField>
              </div>
          </template> 
            <template #list="slotProps">
                <div class="grid grid-nogutter">
                    <div v-for="(item, index) in slotProps.items" :key="index" class="col-12">
                        <div class="flex flex-column sm:flex-row sm:align-items-center p-4 gap-3" :class="{ 'border-top-1 surface-border': index !== 0 }">
                            <div class="flex flex-column md:flex-row justify-content-between md:align-items-center flex-1 gap-4">
                                <div class="flex flex-row justify-content-center md:align-items-center gap-4">
                                    <div class="flex flex-row md:flex-column justify-content-between align-items-start gap-2">
                                        <div>
                                            <div class="text-lg font-medium text-900 mt-2">{{ item.name }}</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-content-center gap-5">
                                <div class="flex flex-row justify-content-center md:align-items-center gap-4">
                                    <div class="flex flex-row md:flex-column justify-content-between align-items-start gap-2">
                                        <div>
                                            <div class="text-base font-medium text-900 mt-2 text-right">{{ item.date }}</div>
                                            <div class="text-base font-medium text-900 mt-2 text-right">{{ item.numFriendsAttending }} friends attending</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex flex-column md:align-items-end gap-5">
                                    <div class="flex flex-column gap-2">
                                        <span class="text-xl font-semibold text-900">{{ item.points }} points</span>
                                        <Button icon="pi pi-ticket" label=" Attend" class="flex-auto " @click="save(item)"></Button>
                                </div>
                                </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </template>
        </DataView>
      
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