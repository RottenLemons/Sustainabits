<script setup lang="ts">
  import { useRoute, useRouter } from 'vue-router';
  import { ref, onBeforeMount, watch } from "vue";
  import { useCookies } from '@vueuse/integrations/useCookies';
  import { activities, getUser, insertAct, searchA } from "@/service/TalkToDB";
  import DataView from 'primevue/dataview';
  import Button from 'primevue/button';
  import Tag from 'primevue/tag';
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
  
  onBeforeMount(async () => {
      let response = await activities(user.growTree ,user.userID, new Date().toISOString().split('T')[0], new Date(user.growStartDate).toISOString().split('T')[0]);
      items.value = response.activities
  });

  
  const save = async (activity: any) => {
    let res1 = await insertAct(user.userID,activity.activityID);
    let response = await activities(user.growTree ,user.userID, new Date().toISOString().split('T')[0], new Date(user.growStartDate).toISOString().split('T')[0]);
    items.value = response.activities
    response = await getUser(user.userID);
    cookies.set('user', response.user);
    user.value = response.user;
  };

  const query = ref('')

    watch(query, async (val) => {
    let response = await searchA(user.growTree ,user.userID, new Date().toISOString().split('T')[0], new Date(user.growStartDate).toISOString().split('T')[0], query.value);
    items.value = response.activities
    });
</script>

<template>
  <main style="width: 100%;">
    <div class="flex flex-column align-items-center justify-content-center" style="backgroundColor: #337357; width: 100%; min-height: 94vh;">
        <p style="font-size: 4em; font-weight: bold; color: white; margin-bottom: 0.75em; margin-top: 0.5em;" class="font">Activities</p>
        <DataView paginator :rows="3" :value="items" dataKey="userID" style="width: 70%;">
            <template #header>
              <div class="flex justify-content-end">
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
                                            <Tag v-if="item.treeAct > 0" value="Tree Activity" severity="success"></Tag>
                                            <div class="text-lg font-medium text-900 mt-2">{{ item.name }}</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex flex-row justify-content-center md:align-items-center gap-4">
                                    <div class="flex flex-row md:flex-column justify-content-between align-items-start gap-2">
                                        <div>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex flex-column md:align-items-end gap-5">
                                    <div class="flex flex-column gap-2">
                                        <span class="text-xl font-semibold text-900">{{ item.points }} points</span>
                                        <Button icon="pi pi-check" label=" Completed" class="flex-auto " @click="save(item)"></Button>
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