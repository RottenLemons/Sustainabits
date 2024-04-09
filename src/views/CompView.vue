<script setup lang="ts">
  import { useRoute, useRouter } from 'vue-router';
  import { ref, onBeforeMount } from "vue";
  import { useCookies } from '@vueuse/integrations/useCookies';
  import { competition, friendChange, joinC } from "@/service/TalkToDB";
  import DataView from 'primevue/dataview';
  import Button from 'primevue/button';
  import Avatar from 'primevue/avatar';
  import Tag from 'primevue/tag';

  const cookies = useCookies()
  const route = useRoute()
  const id = route.params.compID;
  const user = cookies.get('user');
  let router = useRouter();
  if (!user) {
    router.push('/login');
  }
  let item = ref<any>({});
  let items = ref<any[]>([]);

  onBeforeMount(async () => {
        let response = await competition(user.userID, id);
        item.value = response.competition
        items.value = response.participants
  });
  
  const save = async (friend: any) => {
    let response = await friendChange(user.userID, friend.userID, friend.friendID ? false : true);
    if (friend.friendID){   
        items.value[items.value.findIndex((item: any) => item.userID === friend.userID)].friendID = null;
    } else {
        items.value[items.value.findIndex((item: any) => item.userID === friend.userID)].friendID = friend.userID;
    }
  };

  const save2 = async (competition: any) => {
    let res1 = await joinC(user.userID, item.value.competitionID);
    let response = await competition(user.userID, id);
    item.value = response.competition
    items.value = response.participants
  };
</script>

<template>
  <main style="width: 100%;">
    <div class="flex flex-column align-items-center justify-content-center" style="backgroundColor: #337357; width: 100%; min-height: 94vh;">
        <p style="font-size: 4em; font-weight: bold; color: white; margin-bottom: 0.2em; margin-top: 0.5em;" class="font">{{ item.name }}</p>
        <p style="font-size: 2em; color: #dddddd; margin-top: 0.2em;">{{ item.description }}</p>
        <p style="font-size: 2em; font-weight: bold; color: white; margin-top: 0.4em;">{{ item.startDate }} to {{ item.endDate }}</p>
        <DataView v-if="new Date(item.startDate) < new Date()"  paginator :rows="3" :value="items" dataKey="userID" style="width: 70%; margin-bottom: 3em;">
            <template #list="slotProps">
                <div class="grid grid-nogutter">
                    <div v-for="(item, index) in slotProps.items" :key="index" class="col-12">
                        <div class="flex flex-column sm:flex-row sm:align-items-center p-4 gap-3" :class="{ 'border-top-1 surface-border': index !== 0 }">
                            <p class="text-2xl font-large text-900 mr-2">{{ item.rank }}</p>
                            <div class="md:w-10rem relative">
                                <Avatar :image="'../../server/images/'+item.userimage" shape="circle" style="width: 8rem; height: 8rem"/>
                            </div>
                            <div class="flex flex-column md:flex-row justify-content-between md:align-items-center flex-1 gap-4">
                              <div class="flex flex-row justify-content-center md:align-items-center gap-4">
                                    <div class="flex flex-row md:flex-column justify-content-between align-items-start gap-2">
                                        <div>
                                            <Tag v-if="item.friendID" value="Friend" severity="success"></Tag>
                                            <div class="text-lg font-medium text-900 mt-2">{{ item.username }}</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-content-center gap-4 align-items-center">

                                <div class="flex flex-row justify-content-center md:align-items-center gap-4">
                                    <div class="flex flex-row md:flex-column justify-content-between align-items-start gap-2">
                                        <div>
                                            <div class="text-base font-medium text-900 mt-2 text-right">{{ item.countTrees }} Trees made</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex flex-column md:align-items-end gap-5">
                                    <div class="flex flex-column gap-2">
                                        <span class="text-xl font-semibold text-900" style="text-align: end;">{{ item.points }} points</span>
                                        <Button v-if="!item.friendID && item.userID !== user.userID" icon="pi pi-user-plus" label=" Add friend" class="flex-auto " @click="save(item)"></Button>
                                        <Button v-if="item.friendID && item.userID !== user.userID" icon="pi pi-user-minus" label=" Remove friend" class="flex-auto " @click="save(item)"></Button>
                                </div>
                                </div>
                              </div>

                            </div>
                        </div>
                    </div>
                </div>
            </template>
        </DataView>
        <Button v-if="item.participate==0 && new Date(item.startDate) < new Date() && new Date() < new Date(item.endDate)" label=" Join" @click="save2" style="height:3em; width: 70%; margin-bottom: 2rem;"></Button>
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