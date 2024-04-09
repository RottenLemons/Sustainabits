<script setup lang="ts">
  import { useRouter } from 'vue-router';
  import { ref, onBeforeMount, watch } from "vue";
  import { useCookies } from '@vueuse/integrations/useCookies';
  import { competitions, joinC, searchC } from "@/service/TalkToDB";
  import DataView from 'primevue/dataview';
  import Button from 'primevue/button';
  import InputText from 'primevue/inputtext';

  const cookies = useCookies()
  const router = useRouter()
  const user = cookies.get('user');
  let items = ref<any[]>([]);
  const query = ref('')

  watch(query, async (val) => {
    let response = await searchC(user.userID, query.value);
    items.value = response.competitions
  });
  
  onBeforeMount(async () => {
      let response = await competitions(user.userID);
      items.value = response.competitions
  });

  const save = async (competition: any) => {
    let res1 = await joinC(user.userID,competition.competitionID);
    let response = await competitions(user.userID);
    items.value = response.competitions
  };
  
  const save2 = async (competition: any) => {
    router.push('/comps/' + competition.competitionID)
  };
  
  const save3 = async () => {
    router.push('/ccomp')
  };


</script>

<template>
  <main style="width: 100%;">
    <div class="flex flex-column align-items-center justify-content-center" style="backgroundColor: #337357; width: 100%; min-height: 94vh;">
        <p style="font-size: 4em; font-weight: bold; color: white; margin-bottom: 0.75em; margin-top: 0.5em;" class="font">Competitions</p>
        <DataView paginator :rows="4" :value="items" dataKey="userID" style="width: 70%;">
          <template #header>
              <div class="flex justify-content-end">
                  <IconField iconPosition="left">
                      <InputIcon>
                          <i class="pi pi-search" />
                      </InputIcon>
                      <InputText style="margin-left: 1rem;" placeholder="Keyword Search" v-model="query" />
                  </IconField>
              </div>
          </template>  
          <template #list="slotProps">
                <div class="grid grid-nogutter">
                    <div v-for="(item, index) in slotProps.items" :key="index" class="col-12">
                        <div class="flex flex-column sm:flex-row sm:align-items-center p-4 gap-3" :class="{ 'border-top-1 surface-border': index !== 0 }">
                            <div class="flex flex-column md:flex-row justify-content-between md:align-items-center flex-1 gap-4">
                                
                                <div class="flex flex-row justify-content-center md:align-items-center gap-4">
                                    <div class="flex flex-row md:flex-column justify-content-between align-items-start gap-2" @click="save2(item)">
                                        <div>
                                            <div class="text-lg font-medium text-900 mt-2 underline">{{ item.name }}</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-content-center gap-4">
                                <div class="flex flex-row justify-content-center md:align-items-center gap-4">
                                    <div class="flex flex-row md:flex-column justify-content-between align-items-start gap-2">
                                        <div>
                                            <div class="text-base font-medium text-900 mt-2 text-right">{{ item.startDate }}</div>
                                            <div class="text-base font-medium text-900 mt-2 text-right">{{ item.endDate }}</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex flex-column md:align-items-end gap-5">
                                    <div class="flex flex-column gap-2">
                                        <Button v-if="item.participate==0 && new Date(item.startDate) < new Date() && new Date() < new Date(item.endDate)" icon="pi pi-plus-circle" label=" Join" class="flex-auto " @click=save(item)></Button>
                                </div>
                                </div>
                              </div>
                            </div>
                        </div>
                    </div>
                </div>
            </template>
        </DataView>
        <Button label=" Create Competition" style="width: 70%; margin-top: 1rem; margin-bottom: 3rem;" @click="save3"></Button>
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