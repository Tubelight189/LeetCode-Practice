#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *next;
};
struct node *create (int value){
        struct node*p=(struct node*)malloc(sizeof(struct node));
        p->data=value;p->next=NULL;
        return p;
}
void trv(struct node *head)
{
    struct node *p = head;
    while (p != NULL)
    {
        printf("%d -> ", p->data);
        p = p->next;
    }
}
int count(struct node *head)
{
    int c=0;
    struct node *p = head;
    while (p != NULL){c++;p=p->next;}
    return c;
}
 int hcf(int a,int b){
    if(a%b==0)return b;
    if(b%a==0)return a;
    int n=(a>b)?a:b;int max=0;
    for (int i=1;i<=n;i++){
        if (a%i==0&&b%i==0){max=(max<i)?i:max;}
    }
    return max;
 }
void Q(struct node *head) {
    struct node *p=head,*temp=NULL;
   while(p->next!=NULL){
    temp=(struct node*)malloc(sizeof(struct node));
    temp->data=hcf(p->data,p->next->data);
    printf("%d",temp->data);printf("\n");
    temp->next=p->next;
    p->next=temp;
    p=p->next->next;
   } 
   trv(head);
}


void main()
{
    struct node *l1,*l2;
    l1=create(18);
    l1->next=create(6);
    l1->next->next=create(10);
    l1->next->next->next=create(3);
    // l1->next->next->next->next=create(4);
    // l1->next->next->next->next->next=create(4);
    // l1->next->next->next->next->next->next=create(5);

    l2=create(1);
    l2->next=create(1);
    l2->next->next=create(1);
    l2->next->next->next=create(1);
    // trv(l1);
    // printf("\n");
    trv(l1);printf("\n");
    // struct node*a=
    Q(l1);
    // trv(a);

}