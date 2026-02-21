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
struct node* Q(struct node *head) {
    struct node *p = head;
    while (p->next!= NULL){
        if(p->data==p->next->data){
        printf("%d,%d\n",p->data,p->next->data);
            p->next=p->next->next;
            }
            else{
        p = p->next;}
    }
    p->next=NULL;
    return head;
}


void main()
{
    struct node *l1,*l2;
    l1=create(1);
    l1->next=create(2);
    l1->next->next=create(3);
    l1->next->next->next=create(3);
    l1->next->next->next->next=create(4);
    l1->next->next->next->next->next=create(4);
    l1->next->next->next->next->next->next=create(5);

    l2=create(1);
    l2->next=create(3);
    l2->next->next=create(4);
    // l2->next->next->next=create(9);
    trv(l1);
    printf("\n");
    // trv(l2);printf("\n");
    struct node*a=Q(l1);
    trv(a);

}